class Task:
    def __init__(
        self,
        title,
        task_type,
        task_id=None,
        completed=False,
        week_created=None,
        last_completed_week=None,
    ):
        self.id = task_id
        self.title = title
        self.task_type = task_type
        self.completed = completed
        self.week_created = week_created
        self.last_completed_week = last_completed_week
