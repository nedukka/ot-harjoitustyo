import tkinter as tk
from tkinter import ttk
from tkinter import font
from src.ui.add_view import AddTaskView

class MainView:
    def __init__(self, root, task_service):
        self._root = root
        self._task_service = task_service
        self._motivation_level = "LOW"

        self._root.configure(bg="black")

        self._main_container = tk.Frame(self._root, bg="black")
        self._main_container.pack(fill="both", expand=True)

        self._content = tk.Frame(self._main_container, bg="#E6D6F2")
        self._content.pack(fill="both", expand=True, padx=10)

        self._normal_font = font.Font(family="Helvetica", size=12)
        self._completed_font = font.Font(family="Helvetica", size=12, overstrike=1)

        self._build()
        self._update_motivation_buttons()
        self._refresh_tasks()

    def _open_add_task_popup(self):
        AddTaskView(self._root, self._task_service, self._refresh_tasks)

    def _build(self):
        self._content.columnconfigure(0, weight=1)
        self._content.rowconfigure(3, weight=1)

        ttk.Label(
            self._content,
            text="Tehtävät",
            font=("Helvetica", 18)
        ).grid(row=0, column=0, pady=10)

        ttk.Label(
            self._content,
            text="Vaihda motivaatiotasoa:",
            font=("Helvetica", 12)
        ).grid(row=1, column=0, pady=5)

        button_frame = tk.Frame(self._content, bg="#E6D6F2")
        button_frame.grid(row=2, column=0, sticky="ew", padx=40, pady=10)

        button_frame.columnconfigure((0, 1, 2), weight=1)

        self._motivation_buttons = {}

        self._motivation_buttons["LOW"] = tk.Button(
            button_frame,
            text="Matala",
            font=("Helvetica", 12, "bold"),
            command=lambda: self._set_motivation_level("LOW")
        )
        self._motivation_buttons["LOW"].grid(row=0, column=0, sticky="ew", padx=3)

        self._motivation_buttons["MEDIUM"] = tk.Button(
            button_frame,
            text="Keskitaso",
            font=("Helvetica", 12, "bold"),
            command=lambda: self._set_motivation_level("MEDIUM")
        )
        self._motivation_buttons["MEDIUM"].grid(row=0, column=1, sticky="ew", padx=3)

        self._motivation_buttons["HIGH"] = tk.Button(
            button_frame,
            text="Korkea",
            font=("Helvetica", 12, "bold"),
            command=lambda: self._set_motivation_level("HIGH")
        )
        self._motivation_buttons["HIGH"].grid(row=0, column=2, sticky="ew", padx=3)        

        self._task_area = tk.Frame(self._content, bg="white")
        self._task_area.grid(row=3, column=0, sticky="nsew", padx=40, pady=10)

        ttk.Label(
            self._content,
            text="Tehdyt",
            font=("Helvetica", 14)
        ).grid(row=5, column=0, pady=10)

        self._completed_area = tk.Frame(self._content, bg="white")
        self._completed_area.grid(row=6, column=0, sticky="nsew", padx=40, pady=10)

        ttk.Button(
            self._content,
            text="Lisää tehtävä",
            command=self._open_add_task_popup
        ).grid(row=4, column=0, pady=10)

    def _update_motivation_buttons(self):
        for level, button in self._motivation_buttons.items():
            if level == self._motivation_level:
                button.configure(
                    bg="#B57EDC",
                    fg="white",
                    activebackground="#9F63C7"
                )
            else:
                button.configure(
                    bg="#D8BFD8",
                    fg="black",
                    activebackground="#CBA6E3"
                )

    def _set_motivation_level(self, level):
        self._motivation_level = level
        self._update_motivation_buttons()
        self._refresh_tasks()

    def _refresh_tasks(self):
        for widget in self._task_area.winfo_children():
            widget.destroy()
        
        for widget in self._completed_area.winfo_children():
            widget.destroy()

        tasks = self._task_service.get_tasks_by_motivation(self._motivation_level)

        for task in tasks:
            target_area = self._completed_area if task.completed else self._task_area
            frame = ttk.Frame(target_area)
            frame.pack(fill="x", padx=5, pady=2)

            current_font = self._completed_font if task.completed else self._normal_font

            ttk.Label(
                frame, 
                text=task.title, 
                font=current_font
            ).pack(side="left", padx=5)

            if not task.completed:
                ttk.Button(
                    frame,
                    text="✓",
                    command=lambda t=task: self._complete_task(t.id)
                ).pack(side="right", padx=5)
        if not any(not t.completed for t in tasks):
            tk.Label(
                self._task_area,
                text="Tällä tasolla ei ole näkyvissä tehtäviä. Vaihda motivaatiotasoa tai lisää uusia tehtäviä",
                bg="white",
                fg="gray",
                font=("Helvetica", 11, "italic"),
                wraplength=250,
                justify="center"
            ).pack(pady=10)


    def _complete_task(self, task_id):
        self._task_service.complete_task(task_id)
        self._refresh_tasks()

