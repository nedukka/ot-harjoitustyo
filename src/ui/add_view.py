import tkinter as tk
from tkinter import ttk


class AddTaskView:
    def __init__(self, root, task_service, refresh_callback):
        self._root = root
        self._task_service = task_service
        self._refresh_callback = refresh_callback

        self._overlay = tk.Frame(self._root, bg="#FFB4B4")
        self._overlay.place(relx=0, rely=0, relwidth=1, relheight=1)

        self._overlay.lift()

        self._frame = tk.Frame(self._root, bg="#E6D6F2", bd=1, relief="solid")

        self._frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=300,
            height=300
        )

        self._build()

    def _build(self):
        self._frame.columnconfigure(0, weight=1)
        
        self._error_label = tk.Label(
            self._frame,
            text="",
            wraplength=250,
            fg="red",
            font=("Helvetica", 10)
        )
        self._error_label.grid(row=1, column=0, pady=5, sticky="ew")

        ttk.Label(
            self._frame,
            text="Uusi tehtävä",
            font=("Helvetica", 14)
        ).grid(row=0, column=0, pady=10)

        self._entry = ttk.Entry(self._frame)
        self._entry.grid(row=2, column=0, padx=10, sticky="ew")

        self._task_type = tk.StringVar()

        radio_frame = ttk.Frame(self._frame)
        radio_frame.grid(row=3, column=0, pady=15)

        ttk.Radiobutton(
            radio_frame,
            text="tämä viikko",
            variable=self._task_type,
            value="WEEK_SPECIFIC"
        ).pack()

        ttk.Radiobutton(
            radio_frame,
            text="toistuu viikoittain",
            variable=self._task_type,
            value="WEEKLY"
        ).pack()

        ttk.Radiobutton(
            radio_frame,
            text="ajaton",
            variable=self._task_type,
            value="BACKLOG"
        ).pack()

        ttk.Button(
            self._frame,
            text="Lisää",
            command=self._handle_add
        ).grid(row=4, column=0, pady=1)

        ttk.Button(
            self._frame,
            text="Peruuta",
            command=self._close
        ).grid(row=5, column=0, pady=1)

    def _handle_add(self):
        title = self._entry.get()
        task_type = self._task_type.get()

        try:
            self._task_service.add_task(title, task_type)
            self._error_label.config(text="")
            self._refresh_callback()
            self._close()
        except ValueError:
            self._error_label.config(
                text="Tehtävän nimi ei saa olla tyhjä ja tehtävätyypin valinta on pakollinen"
            )

    def _close(self):
        self._frame.destroy()
        self._overlay.destroy()
