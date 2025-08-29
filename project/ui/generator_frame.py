"""Session generator UI frame."""

import customtkinter as ctk

from .preview_frame import PreviewFrame


class GeneratorFrame(ctk.CTkFrame):
    """Frame containing the session generator form and preview."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._build_form()
        self._build_preview()

    def _build_form(self):
        form = ctk.CTkScrollableFrame(self, width=300)
        form.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        form.grid_columnconfigure(0, weight=1)
        row = 0

        name_label = ctk.CTkLabel(form, text="Nom de la séance")
        name_label.grid(row=row, column=0, sticky="w")
        row += 1
        ctk.CTkEntry(form).grid(row=row, column=0, sticky="ew", pady=(0, 10))
        row += 1

        duration_label = ctk.CTkLabel(form, text="Durée (min)")
        duration_label.grid(row=row, column=0, sticky="w")
        row += 1
        duration = ctk.CTkOptionMenu(form, values=["30", "45", "60", "90"])
        duration.set("45")
        duration.grid(row=row, column=0, sticky="ew", pady=(0, 10))
        row += 1

        type_label = ctk.CTkLabel(form, text="Type de séance")
        type_label.grid(row=row, column=0, sticky="w")
        row += 1
        type_menu = ctk.CTkOptionMenu(form, values=["HIIT", "Force", "Endurance", "Mobilité"])
        type_menu.set("HIIT")
        type_menu.grid(row=row, column=0, sticky="ew", pady=(0, 10))
        row += 1

        obj_label = ctk.CTkLabel(form, text="Objectif")
        obj_label.grid(row=row, column=0, sticky="w")
        row += 1
        obj_menu = ctk.CTkOptionMenu(form, values=["Force", "Endurance", "Mobilité"])
        obj_menu.set("Endurance")
        obj_menu.grid(row=row, column=0, sticky="ew", pady=(0, 10))
        row += 1

        equip_label = ctk.CTkLabel(form, text="Matériel", font=ctk.CTkFont(weight="bold"))
        equip_label.grid(row=row, column=0, sticky="w")
        row += 1
        ctk.CTkCheckBox(form, text="Poids de corps").grid(row=row, column=0, sticky="w")
        row += 1
        ctk.CTkCheckBox(form, text="Haltères").grid(row=row, column=0, sticky="w")
        row += 1
        ctk.CTkCheckBox(form, text="Kettlebells").grid(row=row, column=0, sticky="w")
        row += 1
        ctk.CTkCheckBox(form, text="TRX").grid(row=row, column=0, sticky="w", pady=(0, 10))
        row += 1

        var_label = ctk.CTkLabel(form, text="Variabilité")
        var_label.grid(row=row, column=0, sticky="w")
        row += 1
        var_slider = ctk.CTkSlider(form, from_=0, to=100, number_of_steps=100)
        var_slider.set(50)
        var_slider.grid(row=row, column=0, sticky="ew", pady=(0, 10))
        row += 1

        vol_label = ctk.CTkLabel(form, text="Volume")
        vol_label.grid(row=row, column=0, sticky="w")
        row += 1
        vol_slider = ctk.CTkSlider(form, from_=0.5, to=2.0)
        vol_slider.set(1.0)
        vol_slider.grid(row=row, column=0, sticky="ew", pady=(0, 10))
        row += 1

        int_label = ctk.CTkLabel(form, text="Biais intensité")
        int_label.grid(row=row, column=0, sticky="w")
        row += 1
        int_slider = ctk.CTkSlider(form, from_=0, to=100)
        int_slider.set(50)
        int_slider.grid(row=row, column=0, sticky="ew", pady=(0, 10))
        row += 1

        ctk.CTkButton(form, text="Générer", state="disabled").grid(
            row=row, column=0, sticky="ew", pady=20
        )

    def _build_preview(self):
        preview = PreviewFrame(self)
        preview.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.preview = preview
