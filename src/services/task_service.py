from datetime import datetime
from src.repositories.task_repository import TaskRepository
from src.models.task import Task

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, title: str, task_type: str):

        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if task_type not in ["BACKLOG", "WEEKLY", "WEEK_SPECIFIC"]:
            raise ValueError("Invalid task type")

        week_created = None
        if task_type == "WEEK_SPECIFIC":
            week_created = get_current_week()

        task = Task(
            title=title,
            task_type=task_type,
            completed=False,
            week_created=week_created,
            last_completed_week=None,
        )
        return self.repository.create_task(task)

    def complete_task(self, task_id: int):
        task = self.repository.find_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")

        task.completed = True
        task.last_completed_week = get_current_week()
        self.repository.update_task(task)

    def get_tasks_by_motivation(self, motivation_level: str):
        if motivation_level not in ["LOW", "MEDIUM", "HIGH"]:
            raise ValueError("Invalid motivation level")

        tasks = self.repository.get_all_tasks()
        current_week = get_current_week()

        visible_tasks = []
        for task in tasks:

            if task.completed and task.last_completed_week == current_week:
                visible_tasks.append(task)
                continue

            if task.task_type == "WEEKLY" and task.last_completed_week != current_week:
                task.completed = False
            if task.task_type == "WEEK_SPECIFIC" and task.week_created != current_week:
                continue

            if motivation_level == "LOW":
                if task.task_type == "WEEK_SPECIFIC":
                    visible_tasks.append(task)
            elif motivation_level == "MEDIUM":
                if task.task_type in [
                    "WEEK_SPECIFIC",
                    "WEEKLY",
                ]:
                    visible_tasks.append(task)
            else:
                visible_tasks.append(task)

        visible_tasks.sort(key=lambda task: self.task_priority(task.task_type))

        return visible_tasks

    def task_priority(self, task_type: str):
        order = {"WEEK_SPECIFIC": 0, "WEEKLY": 1, "BACKLOG": 2}
        return order.get(task_type, 99)

    def delete_tasks(self, task_ids: list):
        if not task_ids:
            return
        self.repository.delete_tasks_by_ids(task_ids)

def get_current_week():
    return datetime.now().isocalendar()[1]
