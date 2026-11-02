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
            pass
        
        description = 'Valid Id Test Task'
        for valid_id in (1, 2, 42, 1018, SubInt(42)):
            with self.subTest(id = valid_id):
                task = Task(valid_id, description)
                self.assertEqual(task.id, valid_id)

    def test_valid_description(self):
        class StrSubClass(str):
            pass
        
        for value in ('Buy milk', 'a', '💀', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N', 'hi ', StrSubClass('Buy milk')):
            with self.subTest(description = value):
                task = Task(1, value)
                self.assertEqual(task.description, value)

    def test_invalid_description(self):
        for value in ('', ' '):
            with self.subTest(description = value):
                with self.assertRaises(ValueError):
                    Task(1, value)