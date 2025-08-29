import customtkinter as ctk
from .card import Card


class SessionCard(Card):
    """Card specialized for displaying session information."""

    def __init__(
        self,
        master,
        name: str,
        duration: int,
        session_type: str,
        tags: list[str] | None = None,
        objective: str = "",
        **kwargs,
    ):
        description = f"{session_type} - {objective}" if objective else session_type
        super().__init__(
            master,
            title=name,
            value=f"{duration} min",
            description=description,
            **kwargs,
        )
        tags = tags or []
        self.content.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(
            self.content,
            text="Tags: " + ", ".join(tags) if tags else "Tags: -",
        ).grid(row=0, column=0, sticky="w")
