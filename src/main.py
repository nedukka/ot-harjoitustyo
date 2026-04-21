from tkinter import Tk
from src.ui.ui import UI
from src.services.task_service import TaskService
from src.services.user_service import UserService
from src.repositories.task_repository import TaskRepository
from src.repositories.user_repository import UserRepository

def main():

    root = Tk()
    root.title("TBA")
    root.geometry("400x600")

    task_repository = TaskRepository()
    task_service = TaskService(task_repository)

    user_repository = UserRepository()
    user_service = UserService(user_repository)

    ui_screen = UI(root, task_service, user_service)
    ui_screen.start()

    root.mainloop()


if __name__ == "__main__":
    main()
