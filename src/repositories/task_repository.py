from src.database.database_connection import get_database_connection
from src.models.task import Task

class TaskRepository:
    def __init__(self):
        self.connection = get_database_connection()

    def create_task(self, task: Task):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO tasks (
                   title, task_type, completed, week_created, last_completed_week)
                    VALUES (?, ?, ?, ?, ?)
        ''', (task.title, task.task_type, int(task.completed), task.week_created, task.last_completed_week))
        self.connection.commit()

        task.id = cursor.lastrowid
        return task

    def row_to_task(self, row):
        return Task(
            id=row['id'],
            title=row['title'],
            task_type=row['task_type'],
            completed=bool(row['completed']),
            week_created=row['week_created'],
            last_completed_week=row['last_completed_week']
        )

    def get_all_tasks(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tasks')
        rows = cursor.fetchall()

        return [self.row_to_task(row) for row in rows]
    
    def find_task_by_id(self, task_id: int):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()

        if row is None:
            return None
        return self.row_to_task(row)
    
    def update_task(self, task: Task):
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE tasks
            SET title = ?, task_type = ?, completed = ?, week_created = ?, last_completed_week = ?
            WHERE id = ?
        ''', (task.title, task.task_type, int(task.completed), task.week_created, task.last_completed_week, task.id))
        self.connection.commit()
