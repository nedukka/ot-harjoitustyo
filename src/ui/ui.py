from src.ui.front_view import MainView
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.ui.remove_view import RemoveTaskView

class UI:
    def __init__(self, root):
        self._root = root

        repository = TaskRepository()
        self._task_service = TaskService(repository)
        self._current_view = None

    def start(self):
        self._show_main_view()

    def _clear_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_main_view(self):
        self._clear_view()
        self._current_view = MainView(
            self._root, 
            self._task_service,
            self._show_remove_view
        )
        self._current_view.pack(fill="both", expand=True)

    def _show_remove_view(self):
        self._clear_view()
        self._current_view = RemoveTaskView(
            self._root,
            self._task_service,
            self._show_main_view
        )
        self._current_view.pack(fill="both", expand=True)
