import unittest
from src.services.task_service import TaskService
from src.repositories.task_repository import TaskRepository
from src.database.initialize_database import initialize_database

class TestTaskService(unittest.TestCase):

    def setUp(self):
        initialize_database()
        self.repository = TaskRepository()
        self.service = TaskService(self.repository)

    def test_add_task_with_valid_parameters_creates_task(self):
        task = self.service.add_task("Test Task", "WEEKLY")
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.task_type, "WEEKLY")
        self.assertFalse(task.completed)

    def test_add_task_with_empty_title_raises_exception(self):
        with self.assertRaises(ValueError):
            self.service.add_task("", "WEEKLY")

    def test_add_task_with_invalid_type_raises_exception(self):
        with self.assertRaises(ValueError):
            self.service.add_task("Test Task", "MONTHLY")

    def test_task_created_with_week_specific_type_has_week_created_not_None(self):
        task = self.service.add_task("Specific Task", "WEEK_SPECIFIC")
        self.assertIsNotNone(task.week_created)

    def test_complete_task_marks_task_completed(self):
        task = self.service.add_task("Complete Me", "WEEKLY")
        self.service.complete_task(task.id)

        updated_task = self.repository.find_task_by_id(task.id)
        self.assertTrue(updated_task.completed)

    def test_complete_task_with_invalid_id_raises_exception(self):
        with self.assertRaises(ValueError):
            self.service.complete_task(00000)

    def test_get_tasks_by_motivation_with_valid_motivation_level_low_returns_correct(self):
        self.service.add_task("Specific Task", "WEEK_SPECIFIC")
        tasks = self.service.get_tasks_by_motivation("LOW")
        self.assertEqual(len(tasks), 1)
    
    def test_get_tasks_by_motivation_with_valid_motivation_level_medium_returns_correct(self):
        self.service.add_task("Specific Task", "WEEK_SPECIFIC")
        self.service.add_task("Weekly Task", "WEEKLY")
        tasks = self.service.get_tasks_by_motivation("MEDIUM")
        self.assertEqual(len(tasks), 2)
        self.assertIn(tasks[0].task_type, ["WEEK_SPECIFIC", "WEEKLY"])
        self.assertIn(tasks[1].task_type, ["WEEK_SPECIFIC", "WEEKLY"])

    def test_get_tasks_by_motivation_with_valid_motivation_level_high_returns_correct(self):
        self.service.add_task("Specific Task", "WEEK_SPECIFIC")
        self.service.add_task("Weekly Task", "WEEKLY")
        self.service.add_task("Backlog Task", "BACKLOG")

        tasks = self.service.get_tasks_by_motivation("HIGH")
        self.assertEqual(len(tasks), 3)
        self.assertIn(tasks[0].task_type, ["WEEK_SPECIFIC", "WEEKLY", "BACKLOG"])
        self.assertIn(tasks[1].task_type, ["WEEK_SPECIFIC", "WEEKLY", "BACKLOG"])
        self.assertIn(tasks[2].task_type, ["WEEK_SPECIFIC", "WEEKLY", "BACKLOG"])

    def test_get_tasks_by_motivation_with_invalid_motivation_level_raises_exception(self):
        with self.assertRaises(ValueError):
            self.service.get_tasks_by_motivation("EXTREME")

    def test_ignore_week_spesific_task_if_not_created_this_week(self):
        task = self.service.add_task("Old Specific Task", "WEEK_SPECIFIC")
        task.week_created -= 1
        self.repository.update_task(task)

        tasks = self.service.get_tasks_by_motivation("HIGH")
        self.assertNotIn(task, tasks)

    def test_low_motivation_does_not_show_weekly_tasks(self):
        weekly_task = self.service.add_task("Weekly Task", "WEEKLY")
        tasks = self.service.get_tasks_by_motivation("LOW")
        self.assertNotIn(weekly_task, tasks)

    def test_medium_motivation_does_not_show_backlog_tasks(self):
        backlog_task = self.service.add_task("Backlog Task", "BACKLOG")
        tasks = self.service.get_tasks_by_motivation("MEDIUM")
        self.assertNotIn(backlog_task, tasks)

    def test_completed_tasks_are_shown_if_completed_this_week(self):
        task = self.service.add_task("Task to Complete", "WEEK_SPECIFIC")
        self.service.complete_task(task.id)

        tasks = self.service.get_tasks_by_motivation("HIGH")
        task_ids = [t.id for t in tasks]
        self.assertIn(task.id, task_ids)

    def test_delete_tasks_with_valid_ids_deletes_tasks(self):
        task1 = self.service.add_task("Task 1", "WEEKLY")
        task2 = self.service.add_task("Task 2", "BACKLOG")

        self.service.delete_tasks([task1.id, task2.id])

        self.assertIsNone(self.repository.find_task_by_id(task1.id))
        self.assertIsNone(self.repository.find_task_by_id(task2.id))

    def test_delete_tasks_with_empty_id_list_does_nothing(self):
        task = self.service.add_task("Task to Keep", "WEEKLY")
        self.service.delete_tasks([])
        self.assertIsNotNone(self.repository.find_task_by_id(task.id))
