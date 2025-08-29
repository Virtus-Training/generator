"""Frame for listing and managing sessions."""

import customtkinter as ctk

from .components.session_card import SessionCard
from .mock_data import get_mock_sessions


class SessionsFrame(ctk.CTkFrame):
    """UI frame displaying a searchable and filterable list of sessions."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.sessions = get_mock_sessions()
        self.filtered_sessions = list(self.sessions)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build_topbar()
        self._build_cards()

    # Top bar with search and filter button
    def _build_topbar(self):
        top = ctk.CTkFrame(self)
        top.grid(row=0, column=0, sticky="ew")
        top.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(top, text="Recherche").grid(row=0, column=0, padx=5, pady=5)
        self.search_var = ctk.StringVar()
        self.search_var.trace("w", lambda *_: self.update_display())
        ctk.CTkEntry(top, textvariable=self.search_var).grid(
            row=0, column=1, padx=5, pady=5, sticky="ew"
        )

        ctk.CTkButton(top, text="Filtrer", command=self.toggle_filters).grid(
            row=0, column=2, padx=5, pady=5
        )

        self.filter_panel = ctk.CTkFrame(self)
        self.filter_visible = False
        self._build_filters()

    def _build_filters(self):
        self.filter_panel.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(self.filter_panel, text="Date").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.date_var = ctk.StringVar()
        date_entry = ctk.CTkEntry(self.filter_panel, textvariable=self.date_var)
        date_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        date_entry.bind("<KeyRelease>", lambda e: self.update_display())

        ctk.CTkLabel(self.filter_panel, text="Objectif").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        objectives = ["Tous"] + sorted({s["objective"] for s in self.sessions})
        self.objective_var = ctk.StringVar(value="Tous")
        ctk.CTkOptionMenu(
            self.filter_panel,
            variable=self.objective_var,
            values=objectives,
            command=lambda _: self.update_display(),
        ).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self.filter_panel, text="Tag").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.tag_var = ctk.StringVar()
        tag_entry = ctk.CTkEntry(self.filter_panel, textvariable=self.tag_var)
        tag_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        tag_entry.bind("<KeyRelease>", lambda e: self.update_display())

    # Cards grid
    def _build_cards(self):
        self.cards_frame = ctk.CTkFrame(self)
        self.cards_frame.grid(row=2, column=0, sticky="nsew")
        self.update_display()

    def toggle_filters(self):
        if self.filter_visible:
            self.filter_panel.grid_forget()
            self.filter_visible = False
        else:
            self.filter_panel.grid(row=1, column=0, sticky="ew")
            self.filter_visible = True

    def update_display(self):
        search = self.search_var.get().lower()
        objective = self.objective_var.get()
        tag = self.tag_var.get().lower()
        date = self.date_var.get()

        self.filtered_sessions = []
        for sess in self.sessions:
            if search and search not in sess["name"].lower():
                continue
            if objective != "Tous" and sess["objective"] != objective:
                continue
            if tag and not any(tag in t.lower() for t in sess["tags"]):
                continue
            if date and date not in sess["date"]:
                continue
            self.filtered_sessions.append(sess)

        for w in self.cards_frame.winfo_children():
            w.destroy()

        cols = 3
        for idx, sess in enumerate(self.filtered_sessions):
            card = SessionCard(
                self.cards_frame,
                name=sess["name"],
                duration=sess["duration"],
                session_type=sess["type"],
                tags=sess["tags"],
                objective=sess["objective"],
            )
            r, c = divmod(idx, cols)
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

        for c in range(cols):
            self.cards_frame.grid_columnconfigure(c, weight=1)
