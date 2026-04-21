from src.ui.front_view import MainView
from src.ui.remove_view import RemoveTaskView
from src.ui.create_user_view import CreateUserView

class UI:
    def __init__(self, root, task_service, user_service):
        self._root = root

        self._task_service = task_service
        self._user_service = user_service
        self._current_view = None

    def start(self):
        self._show_initial_view()
    
    def _show_initial_view(self):
        user = self._user_service.get_current_user()

        if user is None:
            self._show_create_user_view()
        else:
            self._show_main_view()

    def _show_create_user_view(self):
        self._clear_view()
        self._current_view = CreateUserView(
            self._root, 
            self._user_service,
            self._show_main_view
        )
        self._current_view.pack(fill="both", expand=True)

    def _clear_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_main_view(self):
        self._clear_view()
        self._current_view = MainView(
            self._root, 
            self._task_service,
            self._user_service,
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
