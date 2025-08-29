"""Dashboard frame displaying KPIs and quick actions."""

import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    """Home dashboard for the application."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # KPI tiles
        kpi1 = ctk.CTkFrame(self)
        kpi1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        ctk.CTkLabel(kpi1, text="Séances générées\n12", justify="center").pack(expand=True)

        kpi2 = ctk.CTkFrame(self)
        kpi2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        ctk.CTkLabel(kpi2, text="Clients actifs\n5", justify="center").pack(expand=True)

        # Quick actions
        actions = ctk.CTkFrame(self)
        actions.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
        actions.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkButton(actions, text="Nouvelle séance").grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        ctk.CTkButton(actions, text="Importer séance").grid(row=0, column=1, padx=20, pady=20, sticky="ew")
