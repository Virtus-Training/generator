from .card import Card


class ExerciseCard(Card):
    """Card specialized for displaying exercise information."""

    def __init__(self, master, name: str, details: str = "", **kwargs):
        super().__init__(master, title=name, description=details, **kwargs)
