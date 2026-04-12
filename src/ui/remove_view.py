import tkinter as tk
from tkinter import ttk

class RemoveTaskView(tk.Frame):
    def __init__(self, root, task_service, go_back):
        super().__init__(root)

        self._task_service = task_service
        self._go_back = go_back
        self._variables = []

        self.configure(bg="black")

        self._content = tk.Frame(self, bg="#E6D6F2")
        self._content.pack(fill="both", expand=True, padx=10, pady=10)

        self._build()

    def _build(self):

        self._content.columnconfigure(0, weight=1)
        self._content.rowconfigure(1, weight=1)

        ttk.Label(
            self._content,
            text="Valitse poistettavat tehtävät",
            font=("Helvetica", 14)
        ).grid(row=0, column=0, pady=10)

        self._task_frame = tk.Frame(self._content, bg="white")
        self._task_frame.grid(row=1, column=0, pady=10, sticky="nsew")

        self._task_frame.columnconfigure(0, weight=1)

        self._load_tasks()

        button_frame = ttk.Frame(self._content)
        button_frame.grid(row=2, column=0, pady=10, sticky="ew")
        button_frame.columnconfigure((0, 1), weight=1)

        ttk.Button(
            button_frame,
            text="Poista valitut",
            command=self._delete_selected_tasks
        ).grid(row=2, column=0, padx=6, sticky="ew")

        ttk.Button(
            button_frame,
            text="Takaisin",
            command=self._go_back
        ).grid(row=2, column=1, padx=6, sticky="ew")

    def _load_tasks(self):
        tasks = self._task_service.get_tasks_by_motivation("HIGH")

        for task in tasks:
            if task.completed:
                continue

            var = tk.BooleanVar()
            self._variables.append((var, task.id))

            frame = tk.Frame(self._task_frame)
            frame.pack(fill="x", padx=5, pady=5)

            ttk.Checkbutton(
                frame,
                variable=var
            ).pack(side="left")

            ttk.Label(
                frame,
                text=task.title
            ).pack(side="left", padx=5)

    def _delete_selected_tasks(self):
        selected_ids = [task_id for var, task_id in self._variables if var.get()]
        self._task_service.delete_tasks(selected_ids)
        self._go_back()
