"""Preview frame for displaying generated sessions."""

import customtkinter as ctk
from .mock_data import get_mock_session


class PreviewFrame(ctk.CTkFrame):
    """Frame used to render a session preview."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self._content = ctk.CTkFrame(self)
        self._content.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self._content.grid_columnconfigure(0, weight=1)
        self.render_session()

    def render_session(self, session_data=None):
        """Render the given session data. Uses mock data by default."""
        if session_data is None:
            session_data = get_mock_session()

        for widget in self._content.winfo_children():
            widget.destroy()

        row = 0
        title = ctk.CTkLabel(
            self._content,
            text=session_data.get("name", "Séance"),
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        title.grid(row=row, column=0, sticky="w")
        row += 1

        info = ctk.CTkLabel(
            self._content,
            text=f"Durée : {session_data.get('duration', '?')} min | Objectif : {session_data.get('objective', '')}",
        )
        info.grid(row=row, column=0, sticky="w", pady=(0, 10))
        row += 1

        for block in session_data.get("blocks", []):
            block_lbl = ctk.CTkLabel(
                self._content,
                text=block.get("type", "Bloc"),
                font=ctk.CTkFont(weight="bold"),
            )
            block_lbl.grid(row=row, column=0, sticky="w")
            row += 1
            for ex in block.get("exercises", []):
                ex_lbl = ctk.CTkLabel(
                    self._content,
                    text=f"• {ex.get('name', '')} - {ex.get('details', '')}",
                )
                ex_lbl.grid(row=row, column=0, sticky="w", padx=10)
                row += 1
            if block.get("details"):
                details_lbl = ctk.CTkLabel(self._content, text=block["details"])
                details_lbl.grid(row=row, column=0, sticky="w", padx=10)
                row += 1
