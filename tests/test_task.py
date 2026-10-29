import unittest
from src.task import Task


class TestTaskInit(unittest.TestCase):
    def test_invalid_id_types(self):
        for bad_value in ('1', 1.2, True):
            with self.subTest(id=bad_value):
                with self.assertRaises(TypeError):
                    Task(bad_value, 'Type Error Test Task')  # pyright: ignore[reportArgumentType]

    def test_invalid_id_values(self):
        for bad_value in (-1, 0):
            with self.subTest(id=bad_value):
                with self.assertRaises(ValueError):
                    Task(bad_value, 'Value Error Test Task')

    def test_valid_id(self):
        description = 'Valid Id Test Task'
        task=Task(id=1, description=description)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, description)