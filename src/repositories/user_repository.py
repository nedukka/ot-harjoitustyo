from src.database.database_connection import get_database_connection
from src.models.user import User

class UserRepository:
    def __init__(self):
        self.connection = get_database_connection()

    def create_user(self, user: User):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO users (nickname) VALUES (?)", (user.nickname,))
        self.connection.commit()

        user.id = cursor.lastrowid
        return user

    def get_user(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users LIMIT 1")
        row = cursor.fetchone()

        if row is None:
            return None
        return User(user_id=row["id"], nickname=row["nickname"])
