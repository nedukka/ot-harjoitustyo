import tkinter as tk
from tkinter import ttk

class CreateUserView(tk.Frame):
    def __init__(self, root, user_service, on_user_created):
        super().__init__(root)
        self._user_service = user_service
        self._on_user_created = on_user_created

        self.configure(bg='black')

        self._content = tk.Frame(self, bg='#E6D6F2')
        self._content.pack(fill='both', expand=True, padx=10, pady=10)

        self._build()

    def _build(self):
        self._content.columnconfigure(0, weight=1)

        ttk.Label(
            self._content,
            text="Tervetuloa tehtävälistaan!",
            font=("Helvetica", 18)
        ).grid(row=0, column=0, pady=20)

        ttk.Label(
            self._content,
            text="Aseta nimimerkki aloittaaksesi",
            font=("Helvetica", 12)
        ).grid(row=1, column=0, pady=10)

        self._entry = ttk.Entry(self._content)
        self._entry.grid(row=2, column=0, padx=10, pady=20, sticky="ew")

        self._error_label = tk.Label(
            self._content,
            text="",
            fg="red",
            font=("Helvetica", 10)
        )
        self._error_label.grid(row=3, column=0, pady=5, sticky="ew")

        ttk.Button(
            self._content,
            text="Tallenna ja aloita",
            command=self._create_user
        ).grid(row=4, column=0, pady=20)

    def _create_user(self):
        nickname = self._entry.get()
        try:
            self._user_service.add_user(nickname)
            self._error_label.config(text="")
            self._on_user_created()
        except ValueError:
            self._error_label.config(
                text="Nimimerkki ei voi olla tyhjä. Syötä kelvollinen nimimerkki."
            )
