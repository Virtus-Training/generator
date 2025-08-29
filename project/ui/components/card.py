import customtkinter as ctk


class Card(ctk.CTkFrame):
    """Generic card widget used as a container for displaying information.

    Parameters
    ----------
    master : widget
        Parent widget.
    title : str
        Title displayed at the top of the card.
    value : str
        Main value or highlight shown below the title.
    description : str
        Descriptive text placed under the value.
    **kwargs : Any
        Additional arguments forwarded to :class:`CTkFrame`.
    """

    def __init__(self, master, title="", value="", description="", **kwargs):
        super().__init__(master, corner_radius=8, fg_color=("gray85", "gray20"), **kwargs)

        self.grid_columnconfigure(0, weight=1)
        # Title
        self.title_label = ctk.CTkLabel(self, text=title)
        self.title_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

        # Main value
        self.value_label = ctk.CTkLabel(
            self, text=value, font=ctk.CTkFont(size=20, weight="bold")
        )
        self.value_label.grid(row=1, column=0, sticky="w", padx=10)

        # Description
        self.description_label = ctk.CTkLabel(self, text=description)
        self.description_label.grid(row=2, column=0, sticky="w", padx=10, pady=(0, 10))

        # Container frame for additional widgets
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.grid_rowconfigure(3, weight=1)
