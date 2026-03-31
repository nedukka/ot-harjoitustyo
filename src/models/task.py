class Task:
    def __init__(
        self,
        title: str,
        task_type: str,
        id: int | None = None,
        completed: bool = False,
        week_created: int | None = None,
        last_completed_week: int | None = None,
    ):

        self.id = id
        self.title = title
        self.task_type = task_type
        self.completed = completed
        self.week_created = week_created
        self.last_completed_week = last_completed_week

