import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Estudar Python")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_remove_task(self):
        self.manager.add_task("Teste")
        self.assertTrue(self.manager.remove_task("Teste"))

    def test_remove_nonexistent(self):
        self.assertFalse(self.manager.remove_task("Nada"))

    def test_list_tasks(self):
        self.manager.add_task("A")
        self.manager.add_task("B")
        self.assertEqual(
            self.manager.list_tasks(),
            ["A", "B"]
        )


if __name__ == "__main__":
    unittest.main()