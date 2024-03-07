#!/usr/bin/python3
"""Tests for the User class"""
import os
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    """------------------ BASIC INITIALIZATION ------------------"""

    def test_base_case(self):
        """Test to check if instance of User is properly created"""
        usr = User()
        self.assertIsInstance(usr, User)

    def test_user_inheritance(self):
        """Test to check if User inherits from BaseModel"""
        usr = User()
        self.assertIsInstance(usr, BaseModel)

    """------------------ ATTRIBUTES ------------------"""

    def test_user_id_is_string(self):
        """Test to check if id is a string"""
        usr = User()
        self.assertIsInstance(usr.id, str)

    def test_user_id_is_unique(self):
        """Test to check if id is unique"""
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def test_email_is_string(self):
        """Test to check if email is a string"""
        usr = User()
        self.assertIsInstance(usr.email, str)

    def test_email_is_empty_string(self):
        """Test to check if email is an empty string"""
        usr = User()
        self.assertEqual(usr.email, "")

    def test_password_is_string(self):
        """Test to check if password is a string"""
        usr = User()
        self.assertIsInstance(usr.password, str)

    def test_password_is_empty_string(self):
        """Test to check if password is an empty string"""
        usr = User()
        self.assertEqual(usr.password, "")

    def test_first_name_is_string(self):
        """Test to check if first_name is a string"""
        usr = User()
        self.assertIsInstance(usr.first_name, str)

    def test_first_name_is_empty_string(self):
        """Test to check if first_name is an empty string"""
        usr = User()
        self.assertEqual(usr.first_name, "")

    def test_last_name_is_string(self):
        """Test to check if last_name is a string"""
        usr = User()
        self.assertIsInstance(usr.last_name, str)

    def test_last_name_is_empty_string(self):
        """Test to check if last_name is an empty string"""
        usr = User()
        self.assertEqual(usr.last_name, "")

    def test_created_at_is_datetime(self):
        """Test to check if created_at is a datetime object"""
        usr = User()
        self.assertIsInstance(usr.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """Test to check if updated_at is a datetime object"""
        usr = User()
        self.assertIsInstance(usr.updated_at, datetime.datetime)

    """------------------ TESTS METHODS ------------------"""

    def test_init_method(self):
        """Test to check if instance of User is properly created"""
        usr = User()
        self.assertTrue(hasattr(usr, "email"))
        self.assertTrue(hasattr(usr, "password"))
        self.assertTrue(hasattr(usr, "first_name"))
        self.assertTrue(hasattr(usr, "last_name"))

    def test_str_method(self):
        """Test to check if __str__ method works properly"""
        usr = User()
        name = str(usr.__class__.__name__)
        dico = str(usr.__dict__)
        expected = "[{}] ({}) {}".format(name, usr.id, dico)
        self.assertEqual(str(usr), expected)

    def test_save_method(self):
        """Test to check if save method works properly"""
        usr = User()
        old_save = usr.updated_at
        usr.save()
        self.assertNotEqual(old_save, usr.updated_at)
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict_method(self):
        """Test to check if to_dict method works properly"""
        usr = User()
        expected = {
            "id": usr.id,
            "__class__": "User",
            "created_at": usr.created_at.isoformat(),
            "updated_at": usr.updated_at.isoformat(), }
        self.assertDictEqual(usr.to_dict(), expected)