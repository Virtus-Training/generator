"""Frame for listing and managing exercises."""

import customtkinter as ctk

from .components.exercise_card import ExerciseCard
from .mock_data import get_mock_exercises


class ExercisesFrame(ctk.CTkFrame):
    """UI frame displaying a searchable and filterable list of exercises."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.exercises = get_mock_exercises()
        self.filtered_exercises = list(self.exercises)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build_topbar()
        self._build_cards()

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
        ctk.CTkButton(top, text="Ajouter un exercice").grid(
            row=0, column=3, padx=5, pady=5
        )

        self.filter_panel = ctk.CTkFrame(self)
        self.filter_visible = False
        self._build_filters()

    def _build_filters(self):
        self.filter_panel.grid_columnconfigure(1, weight=1)

        categories = ["Tous"] + sorted({e["category"] for e in self.exercises})
        levels = ["Tous"] + sorted({e["level"] for e in self.exercises})
        equipments = ["Tous"] + sorted({e["equipment"] for e in self.exercises})

        ctk.CTkLabel(self.filter_panel, text="Catégorie").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        self.category_var = ctk.StringVar(value="Tous")
        ctk.CTkOptionMenu(
            self.filter_panel,
            variable=self.category_var,
            values=categories,
            command=lambda _: self.update_display(),
        ).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self.filter_panel, text="Niveau").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.level_var = ctk.StringVar(value="Tous")
        ctk.CTkOptionMenu(
            self.filter_panel,
            variable=self.level_var,
            values=levels,
            command=lambda _: self.update_display(),
        ).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self.filter_panel, text="Matériel").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.equipment_var = ctk.StringVar(value="Tous")
        ctk.CTkOptionMenu(
            self.filter_panel,
            variable=self.equipment_var,
            values=equipments,
            command=lambda _: self.update_display(),
        ).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(self.filter_panel, text="Muscle").grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )
        self.muscle_var = ctk.StringVar()
        muscle_entry = ctk.CTkEntry(self.filter_panel, textvariable=self.muscle_var)
        muscle_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        muscle_entry.bind("<KeyRelease>", lambda e: self.update_display())

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
        category = self.category_var.get()
        level = self.level_var.get()
        equipment = self.equipment_var.get()
        muscle = self.muscle_var.get().lower()

        self.filtered_exercises = []
        for ex in self.exercises:
            if search and search not in ex["name"].lower():
                continue
            if category != "Tous" and ex["category"] != category:
                continue
            if level != "Tous" and ex["level"] != level:
                continue
            if equipment != "Tous" and ex["equipment"] != equipment:
                continue
            if muscle and not any(muscle in m.lower() for m in ex["muscles"]):
                continue
            self.filtered_exercises.append(ex)

        for w in self.cards_frame.winfo_children():
            w.destroy()

        cols = 3
        for idx, ex in enumerate(self.filtered_exercises):
            card = ExerciseCard(
                self.cards_frame,
                name=ex["name"],
                level=ex["level"],
                muscles=ex["muscles"],
                equipment=ex["equipment"],
            )
            r, c = divmod(idx, cols)
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

        for c in range(cols):
            self.cards_frame.grid_columnconfigure(c, weight=1)
