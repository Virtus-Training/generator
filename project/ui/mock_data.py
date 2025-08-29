"""Mock data for UI testing."""


def get_mock_session():
    """Return a mock training session for preview purposes."""
    return {
        "name": "Séance Full-body mock",
        "duration": 45,
        "objective": "Endurance",
        "blocks": [
            {
                "type": "Warmup",
                "exercises": [
                    {"name": "Jumping Jacks", "details": "3 min"},
                    {"name": "Squat Poids de corps", "details": "15 reps"},
                ],
            },
            {
                "type": "Circuit",
                "exercises": [
                    {"name": "Kettlebell Swing", "details": "15 reps"},
                    {"name": "Push Up", "details": "10 reps"},
                    {"name": "Inverted Row", "details": "10 reps"},
                    {"name": "Plank", "details": "30 sec"},
                ],
                "details": "3 tours",
            },
        ],
    }
