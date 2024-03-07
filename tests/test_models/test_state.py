#!/usr/bin/python3
"""Tests for the State class"""
import os
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Tests for the State class"""

    """------------------ BASIC INITIALIZATION ------------------"""

    def test_base_case(self):
        """Test to check if instance of State is properly created"""
        st = State()
        self.assertIsInstance(st, State)

    def test_state_inheritance(self):
        """Test to check if State inherits from BaseModel"""
        st = State()
        self.assertIsInstance(st, BaseModel)

    """------------------ ATTRIBUTES ------------------"""

    def test_state_id_is_string(self):
        """Test to check if id is a string"""
        st = State()
        self.assertIsInstance(st.id, str)

    def test_name_is_string(self):
        """Test to check if name is a string"""
        st = State()
        self.assertIsInstance(st.name, str)

    def test_name_is_empty_string(self):
        """Test to check if name is an empty string"""
        st = State()
        self.assertEqual(st.name, "")

    """------------------ TESTS METHODS ------------------"""

    def test_init_method(self):
        """Test to check if instance of State is properly created"""
        st = State()
        self.assertTrue(hasattr(st, "id"))

    def test_str_method(self):
        """Test to check if __str__ method works properly"""
        st = State()
        name = str(st.__class__.__name__)
        dico = str(st.__dict__)
        expected = "[{}] ({}) {}".format(name, st.id, dico)
        self.assertEqual(str(st), expected)

    def test_save_method(self):
        """Test to check if save method works properly"""
        st2 = State()
        old_save = st2.updated_at
        st2.save()
        self.assertNotEqual(old_save, st2.updated_at)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test to check if to_dict method works properly"""
        st3 = State()
        expected = {
            "id": st3.id,
            "__class__": "State",
            "created_at": st3.created_at.isoformat(),
            "updated_at": st3.updated_at.isoformat(), }
        self.assertDictEqual(st3.to_dict(), expected)