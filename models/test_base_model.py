
import unittest
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_to_dict(self):
        base_instance = BaseModel()
        expected_dict = {
            'id': base_instance.id,
            'created_at': base_instance.created_at.isoformat(),
            'updated_at': base_instance.updated_at.isoformat()
        }
        self.assertEqual(base_instance.to_dict(), expected_dict)

    # Add more test cases for other methods and functionalities

if __name__ == '__main__':
    unittest.main()
