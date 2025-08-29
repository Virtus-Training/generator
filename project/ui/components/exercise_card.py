import customtkinter as ctk
from .card import Card


class ExerciseCard(Card):
    """Card specialized for displaying exercise information."""

    def __init__(
        self,
        master,
        name: str,
        level: str = "",
        muscles: list[str] | None = None,
        equipment: str = "",
        details: str = "",
        **kwargs,
    ):
        super().__init__(master, title=name, value=level, description=details, **kwargs)
        muscles = muscles or []
        self.content.grid_columnconfigure(0, weight=1)
        if muscles:
            ctk.CTkLabel(
                self.content, text="Muscles: " + ", ".join(muscles)
            ).grid(row=0, column=0, sticky="w")
            row = 1
        else:
            row = 0
        if equipment:
            ctk.CTkLabel(
                self.content, text="Équipement: " + equipment
            ).grid(row=row, column=0, sticky="w")

