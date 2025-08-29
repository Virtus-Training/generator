"""Session generation algorithm."""
from __future__ import annotations
import random
from dataclasses import dataclass
from typing import Dict, List

from . import models


class GenerationError(Exception):
    """Raised when a session cannot be generated."""


# Default parameters
DEFAULT_PARAMS = {
    "available_equipment": ["Bodyweight"],
    "group_size": 8,
    "variability": 50,
    "volume_factor": 1.0,
    "session_format": "Blocs",
    "block_types_allowed": ["Circuit", "EMOM", "For Time"],
    "intensity_bias": 50,
    "focus": "Full-body",
    "objective": "Endurance",
    "include_warmup": True,
    "include_cooldown": True,
    "rest_intra_min_sec": (15, 30),
    "rest_inter_min_sec": (30, 60),
}

FOCUS_PATTERNS = {
    "Full-body": ["push", "pull", "squat", "core", "locomotion"],
    "Haut du corps": ["push", "pull"],
    "Bas du corps": ["squat", "hinge"],
    "Push": ["push"],
    "Pull": ["pull"],
    "Core": ["core"],
}

OBJECTIVE_REP_MAP = {
    "Endurance": "20 reps",
    "Force": "5 reps",
    "Hypertrophie": "10 reps",
    "Puissance": "3 reps",
    "Technique": "Practice",
    "Mobilité": "30s hold",
    "Dépense calorique": "30 reps",
}


@dataclass
class GeneratedBlock:
    block: models.Block
    exercises: List[models.ExerciseBlock]



def _merge_params(params: Dict) -> Dict:
    merged = DEFAULT_PARAMS.copy()
    merged.update(params)
    return merged


def _filter_exercises(params: Dict) -> List[models.Exercise]:
    available = set(params["available_equipment"])
    exercises = list(models.Exercise.select())
    filtered = []
    for ex in exercises:
        ex_equip = {e.strip() for e in ex.equipment.split(',')}
        if ex_equip <= available or ex_equip == {"Bodyweight"}:
            filtered.append(ex)
    return filtered


def _score_exercise(ex: models.Exercise, params: Dict) -> float:
    cardio_weight = (100 - params["intensity_bias"]) / 100.0
    strength_weight = params["intensity_bias"] / 100.0
    base = cardio_weight if ex.is_cardio else strength_weight
    focus_patterns = FOCUS_PATTERNS.get(params["focus"], [])
    mult = 1.5 if ex.pattern in focus_patterns else 0.8
    noise_level = params["variability"] / 100.0
    noise = random.uniform(-noise_level, noise_level)
    return base * mult * (1 + noise)


def _assign_reps_or_time(objective: str) -> str:
    return OBJECTIVE_REP_MAP.get(objective, "10 reps")


def generate_session(params: Dict) -> models.Session:
    params = _merge_params(params)
    if params["variability"] == 0:
        random.seed(0)

    exercises = _filter_exercises(params)
    if not exercises:
        raise GenerationError("No exercises after filtering")

    pattern_cycle = FOCUS_PATTERNS.get(params["focus"], ["squat", "push", "pull", "core"])
    core_duration = params["duration_minutes"]
    if params["include_warmup"]:
        core_duration -= int(params["duration_minutes"] * 0.15)
    if params["include_cooldown"]:
        core_duration -= int(params["duration_minutes"] * 0.10)
    n_blocks = max(1, int(core_duration / 10 * params["volume_factor"]))

    chosen_blocks = []
    used_ids = set()
    for i in range(n_blocks):
        pattern = pattern_cycle[i % len(pattern_cycle)]
        candidates = [e for e in exercises if e.pattern == pattern and e.id not in used_ids]
        if not candidates:
            raise GenerationError(f"No exercise for pattern {pattern}")
        scored = sorted(candidates, key=lambda e: _score_exercise(e, params), reverse=True)
        top_n = max(1, round(len(scored) * params["variability"] / 100))
        exercise = random.choice(scored[:top_n])
        used_ids.add(exercise.id)
        block = models.Block(block_type="Core", order=i, duration=600)
        eb = models.ExerciseBlock(block=block, exercise=exercise, order=0,
                                  reps_or_time=_assign_reps_or_time(params["objective"]))
        chosen_blocks.append(GeneratedBlock(block, [eb]))

    # Warmup and cooldown blocks
    blocks = []
    if params["include_warmup"]:
        w_block = models.Block(block_type="Warmup", order=-1, duration=int(params["duration_minutes"] * 0.15 * 60))
        blocks.append(GeneratedBlock(w_block, []))
    blocks.extend(chosen_blocks)
    if params["include_cooldown"]:
        c_block = models.Block(block_type="Cooldown", order=999, duration=int(params["duration_minutes"] * 0.10 * 60))
        blocks.append(GeneratedBlock(c_block, []))

    session = models.Session(
        type=params["type_of_session"],
        duration=params["duration_minutes"],
        format=params["session_format"],
        objective=params["objective"],
        focus=params["focus"],
        volume_factor=params["volume_factor"],
        variability=params["variability"],
        intensity_bias=params["intensity_bias"],
        warmup=params["include_warmup"],
        cooldown=params["include_cooldown"],
    )
    session.blocks_obj = blocks
    return session
