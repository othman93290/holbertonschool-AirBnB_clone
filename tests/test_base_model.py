#!/usr/bin/python3
"""Tests for the BaseModel class"""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    """------------------ SETTING UP ------------------"""

    @classmethod
    def setUpClass(cls):
        """Class method to rename file.json to test_file.json
        and avoid overwriting"""
        cls.base_model = BaseModel()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to rename test_file.json back to file.json"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    """------------------ BASIC INITIALIZATION ------------------"""

    def test_base_case(self):
        """Test to check if instance of BaseModel is properly created"""
        bm0 = BaseModel()
        self.assertIsInstance(bm0, BaseModel)  # true is instance of BaseModel

    """------------------ ATTRIBUTES ------------------"""

    def test_id_is_string(self):
        """Test to check if id is a string"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_id_is_unique(self):
        """Test to check if id is unique"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)  # true if different

    def test_created_at_is_datetime(self):
        """Test to check if created_at is a datetime object"""
        bm2 = BaseModel()
        self.assertIsInstance(bm2.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test to check if updated_at is a datetime object"""
        bm3 = BaseModel()
        self.assertIsInstance(bm3.updated_at, datetime)

    """------------------ TESTS METHODS ------------------"""

    def test_init_method(self):
        """Test to check if instance of BaseModel is properly created"""
        bm0 = BaseModel()
        self.assertTrue(hasattr(bm0, "id"))  # true if bm0 has id
        self.assertTrue(hasattr(bm0, "created_at"))
        self.assertTrue(hasattr(bm0, "updated_at"))

    def test_str_method(self):
        """Test to check if __str__ method works properly"""
        bm1 = BaseModel()
        name = str(bm1.__class__.__name__)
        dico = str(bm1.__dict__)
        expected = "[{}] ({}) {}".format(name, bm1.id, dico)
        self.assertEqual(str(bm1), expected)  # true if both are equal

    def test_save_method(self):
        """Test to check if save method works properly"""
        bm2 = BaseModel()
        old_save = bm2.updated_at
        bm2.save()
        self.assertNotEqual(old_save, bm2.updated_at)  # true old != new
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict_method(self):
        """Test to check if to_dict method works properly"""
        bm3 = BaseModel()
        expected = {
            "id": bm3.id,
            "__class__": bm3.__class__.__name__,
            "created_at": bm3.created_at.isoformat(),
            "updated_at": bm3.updated_at.isoformat()}
        self.assertDictEqual(bm3.to_dict(), expected)  # true if both are equal


if __name__ == "__main__":
    unittest.main()