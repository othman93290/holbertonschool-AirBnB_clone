import unittest
from base_model import BaseModel
from user import User
from file_storage import FileStorage

class TestIntegration(unittest.TestCase):

    def test_create_save_reload_flow(self):
        # Create instances
        user_instance = User(username='john_doe', email='john@example.com')

        # Save instances
        file_storage = FileStorage()
        file_storage.new(user_instance)
        file_storage.save()

        # Reload instances
        new_file_storage = FileStorage()
        new_file_storage.reload()

        # Verify instances are reloaded correctly
        self.assertEqual(new_file_storage.all(), file_storage.all())

if __name__ == '__main__':
    unittest.main()
