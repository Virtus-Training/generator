"""Main application window with navigation."""

import customtkinter as ctk

from .dashboard_frame import DashboardFrame
from .generator_frame import GeneratorFrame


class App(ctk.CTk):
    """Application root class."""

    def __init__(self):
        super().__init__()
        self.title("Générateur de séances")
        self.geometry("900x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._create_sidebar()
        self._create_container()
        self._create_frames()
        self.show_frame("dashboard")

    def _create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=180)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure(5, weight=1)

        ctk.CTkButton(
            self.sidebar, text="Accueil", command=lambda: self.show_frame("dashboard")
        ).grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        ctk.CTkButton(
            self.sidebar, text="Générateur", command=lambda: self.show_frame("generator")
        ).grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        ctk.CTkButton(
            self.sidebar, text="Séances", command=lambda: self.show_frame("sessions")
        ).grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        ctk.CTkButton(
            self.sidebar, text="Exercices", command=lambda: self.show_frame("exercises")
        ).grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        ctk.CTkButton(
            self.sidebar, text="Paramètres", command=lambda: self.show_frame("settings")
        ).grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    def _create_container(self):
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def _create_frames(self):
        self.frames = {
            "dashboard": DashboardFrame(self.container),
            "generator": GeneratorFrame(self.container),
            "sessions": self._placeholder("Séances"),
            "exercises": self._placeholder("Exercices"),
            "settings": self._placeholder("Paramètres"),
        }
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def _placeholder(self, name):
        frame = ctk.CTkFrame(self.container)
        ctk.CTkLabel(
            frame, text=f"Module '{name}' en cours de développement..."
        ).grid(padx=20, pady=20)
        return frame

    def show_frame(self, key):
        frame = self.frames.get(key)
        if frame:
            frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
