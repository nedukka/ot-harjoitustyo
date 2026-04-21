import unittest
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository
from src.database.initialize_database import initialize_database

class TestUserService(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.repository = UserRepository()
        self.service = UserService(self.repository)
        
    def test_create_user_with_valid_nickname_creates_user(self):
        user = self.service.add_user("Testperson")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.nickname, "Testperson")
        
    def test_create_user_with_empty_nickname_raises_exception(self):
        with self.assertRaises(ValueError):
            self.service.add_user("")
            
    def test_get_current_user_returns_user(self):
        current_user = self.service.add_user("CurrentUser")
        current_user = self.service.get_current_user()
        self.assertIsNotNone(current_user)
        self.assertEqual(current_user.nickname, "CurrentUser")