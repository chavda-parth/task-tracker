import unittest
from src.task import Task
from src.task_status import TaskStatus


class TestTaskInit(unittest.TestCase): 
    def test_invalid_id_types(self):      
        for bad_value in ('1', 1.2, True, False, None, [1], (1,), {1:1}, b"1", 1+0j):
            with self.subTest(id=bad_value):
                with self.assertRaises(TypeError):
                    Task(bad_value, 'Type Error Test Task')  # pyright: ignore[reportArgumentType]

    def test_invalid_id_values(self):
        for bad_value in (-1, 0, -10, -10929839):
            with self.subTest(id=bad_value):
                with self.assertRaises(ValueError):
                    Task(bad_value, 'Value Error Test Task')

    def test_valid_id(self):
        class SubInt(int):
            val: int = 284
        
        description = 'Valid Id Test Task'
        for valid_id in (1, 2, 42, 1018, SubInt().val):
            with self.subTest(id = valid_id):
                task = Task(valid_id, description)
                self.assertEqual(task.id, valid_id)

    def test_invalid_description_types(self):
        for bad_value in (1, 1.5, 1.2, True):
            with self.subTest(description = bad_value):
                with self.assertRaises(TypeError):
                    Task(1, bad_value) # pyright: ignore[reportArgumentType]

    def test_invalid_description(self):
        with self.assertRaises(ValueError):
            Task(1, '')

    def test_valid_description(self):
        description = 'Test Description'
        task = Task(1, description)
        self.assertEqual(task.description, description)

    def test_valid_initial_status(self):
        task = Task(1, 'Test task')
        self.assertEqual(task.status, TaskStatus.TODO)    