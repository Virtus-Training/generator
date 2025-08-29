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
                "duration": 10,
                "exercises": [
                    {"name": "Jumping Jacks", "details": "3 min"},
                    {"name": "Squat Poids de corps", "details": "15 reps"},
                ],
            },
            {
                "type": "Circuit",
                "duration": 35,
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


def get_mock_sessions():
    """Return a list of mock sessions for list views."""
    return [
        {
            "name": "Full Body Blast",
            "duration": 60,
            "date": "2024-05-01",
            "type": "collective",
            "objective": "Endurance",
            "tags": ["full-body", "cardio"],
        },
        {
            "name": "Force Maximale",
            "duration": 45,
            "date": "2024-05-03",
            "type": "individuelle",
            "objective": "Force",
            "tags": ["haltères", "poussée"],
        },
        {
            "name": "Yoga Matinal",
            "duration": 30,
            "date": "2024-05-05",
            "type": "collective",
            "objective": "Mobilité",
            "tags": ["souplesse", "respiration"],
        },
        {
            "name": "Cardio Express",
            "duration": 25,
            "date": "2024-05-07",
            "type": "individuelle",
            "objective": "Cardio",
            "tags": ["interval", "HIIT"],
        },
        {
            "name": "Puissance Jambes",
            "duration": 40,
            "date": "2024-05-09",
            "type": "collective",
            "objective": "Hypertrophie",
            "tags": ["jambes", "force"],
        },
        {
            "name": "Core Stability",
            "duration": 35,
            "date": "2024-05-11",
            "type": "individuelle",
            "objective": "Gainage",
            "tags": ["abdos", "stabilité"],
        },
        {
            "name": "Relaxation",
            "duration": 20,
            "date": "2024-05-13",
            "type": "collective",
            "objective": "Récupération",
            "tags": ["douceur", "respiration"],
        },
    ]


def get_mock_exercises():
    """Return a list of mock exercises for list views."""
    return [
        {
            "name": "Pompes",
            "category": "Force",
            "level": "Débutant",
            "muscles": ["Poitrine", "Triceps"],
            "equipment": "Aucun",
        },
        {
            "name": "Squat avec barre",
            "category": "Force",
            "level": "Avancé",
            "muscles": ["Quadriceps", "Fessiers"],
            "equipment": "Barre",
        },
        {
            "name": "Fentes", 
            "category": "Force",
            "level": "Intermédiaire",
            "muscles": ["Quadriceps", "Ischios"],
            "equipment": "Aucun",
        },
        {
            "name": "Burpees",
            "category": "Cardio",
            "level": "Intermédiaire",
            "muscles": ["Full body"],
            "equipment": "Aucun",
        },
        {
            "name": "Planche",
            "category": "Gainage",
            "level": "Débutant",
            "muscles": ["Abdominaux", "Dos"],
            "equipment": "Tapis",
        },
        {
            "name": "Tractions", 
            "category": "Force",
            "level": "Avancé",
            "muscles": ["Dos", "Biceps"],
            "equipment": "Barre de traction",
        },
        {
            "name": "Kettlebell Swing",
            "category": "Cardio",
            "level": "Intermédiaire",
            "muscles": ["Épaules", "Jambes"],
            "equipment": "Kettlebell",
        },
        {
            "name": "Mountain Climbers",
            "category": "Cardio",
            "level": "Débutant",
            "muscles": ["Abdominaux"],
            "equipment": "Aucun",
        },
        {
            "name": "Soulevé de terre",
            "category": "Force",
            "level": "Avancé",
            "muscles": ["Dos", "Jambes"],
            "equipment": "Barre",
        },
        {
            "name": "Crunch",
            "category": "Gainage",
            "level": "Débutant",
            "muscles": ["Abdominaux"],
            "equipment": "Aucun",
        },
        {
            "name": "Dips",
            "category": "Force",
            "level": "Intermédiaire",
            "muscles": ["Triceps", "Pectoraux"],
            "equipment": "Barres parallèles",
        },
        {
            "name": "Sauts à la corde",
            "category": "Cardio",
            "level": "Débutant",
            "muscles": ["Jambes"],
            "equipment": "Corde à sauter",
        },
        {
            "name": "Rowing barre",
            "category": "Force",
            "level": "Intermédiaire",
            "muscles": ["Dos", "Biceps"],
            "equipment": "Barre",
        },
        {
            "name": "Gainage latéral",
            "category": "Gainage",
            "level": "Intermédiaire",
            "muscles": ["Abdominaux", "Obliques"],
            "equipment": "Tapis",
        },
        {
            "name": "Extension triceps poulie",
            "category": "Force",
            "level": "Débutant",
            "muscles": ["Triceps"],
            "equipment": "Poulie",
        },
        {
            "name": "Développé couché",
            "category": "Force",
            "level": "Intermédiaire",
            "muscles": ["Pectoraux", "Triceps"],
            "equipment": "Barre",
        },
        {
            "name": "Tirage horizontal",
            "category": "Force",
            "level": "Débutant",
            "muscles": ["Dos"],
            "equipment": "Machine",
        },
        {
            "name": "Jumping Jacks",
            "category": "Cardio",
            "level": "Débutant",
            "muscles": ["Full body"],
            "equipment": "Aucun",
        },
        {
            "name": "Soulevé de terre jambes tendues",
            "category": "Force",
            "level": "Intermédiaire",
            "muscles": ["Ischios"],
            "equipment": "Barre",
        },
        {
            "name": "Good Morning",
            "category": "Force",
            "level": "Avancé",
            "muscles": ["Lombaires"],
            "equipment": "Barre",
        },
    ]
