from src.repositories.user_repository import UserRepository
from src.models.user import User

class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository
        self._current_user = self._repository.get_user()

    def add_user(self, nickname: str):
        if not nickname.strip():
            raise ValueError("Nickname cannot be empty.")

        user = User(nickname=nickname)
        return self._repository.create_user(user)

    def get_current_user(self):
        return self._repository.get_user()
