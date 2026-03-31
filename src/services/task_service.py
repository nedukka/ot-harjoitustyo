from datetime import datetime
from repositories.task_repository import TaskRepository
from models.task import Task

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, title: str, task_type: str):
 
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if task_type not in ['BACKLOG', 'WEEKLY', 'WEEK_SPESIFIC']:
            raise ValueError("Invalid task type")

        current_week = get_current_week()

        week_created = None
        if task_type == 'WEEK_SPESIFIC':
            week_created = current_week

        task = Task(
            title=title,
            task_type=task_type,
            completed=False,
            week_created=week_created,
            last_completed_week=None
        )
        return self.repository.create_task(task)
 
    def get_tasks_by_motivation(self, motivation_level: str):
        
        tasks = self.repository.get_all_tasks()
        current_week = get_current_week()

        visible_tasks = []
        for task in tasks:
            if task.task_type == 'WEEKLY':
                if task.last_completed_week != current_week:
                    task.completed = False
            if task.task_type == 'WEEK_SPESIFIC':
                if task.week_created != current_week:
                    continue

            if motivation_level not in ['LOW', 'MEDIUM', 'HIGH']:
                raise ValueError("Invalid motivation level")
            
            if motivation_level == 'LOW':
                if task.task_type == 'WEEK_SPESIFIC':
                    visible_tasks.append(task)
            elif motivation_level == 'MEDIUM':
                if task.task_type in ['WEEK_SPESIFIC', 'WEEKLY']:
                    visible_tasks.append(task)
            elif motivation_level == 'HIGH':
                visible_tasks.append(task)

        return visible_tasks

def get_current_week():
    return datetime.now().isocalendar()[1]