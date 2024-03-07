#!/usr/bin/python3
"""Tests for the Review class"""
import os
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Tests for the Review class"""

    """------------------ BASIC INITIALIZATION ------------------"""

    def test_base_case(self):
        """Test to check if instance of Review is properly created"""
        rev = Review()
        self.assertIsInstance(rev, Review)

    def test_review_inheritance(self):
        """Test to check if Review inherits from BaseModel"""
        rev = Review()
        self.assertIsInstance(rev, BaseModel)

    """------------------ ATTRIBUTES ------------------"""

    def test_review_id_is_string(self):
        """Test to check if id is a string"""
        rev = Review()
        self.assertIsInstance(rev.id, str)

    def test_review_id_is_unique(self):
        """Test to check if id is unique"""
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_place_id_is_string(self):
        """Test to check if place_id is a string"""
        rev = Review()
        self.assertIsInstance(rev.place_id, str)

    def test_user_id_is_string(self):
        """Test to check if user_id is a string"""
        rev = Review()
        self.assertIsInstance(rev.user_id, str)

    def test_text_is_string(self):
        """Test to check if text is a string"""
        rev = Review()
        self.assertIsInstance(rev.text, str)

    def test_text_is_empty_string(self):
        """Test to check if text is an empty string"""
        rev = Review()
        self.assertEqual(rev.text, "")

    """------------------ TESTS METHODS ------------------"""

    def test_init_method(self):
        """Test to check if instance of Review is properly created"""
        rev = Review()
        self.assertTrue(hasattr(rev, "place_id"))
        self.assertTrue(hasattr(rev, "user_id"))
        self.assertTrue(hasattr(rev, "text"))

    def test_str_method(self):
        """Test to check if __str__ method works properly"""
        rev = Review()
        name = "Review"
        dico = str(rev.__dict__)
        expected = "[{}] ({}) {}".format(name, rev.id, dico)
        self.assertEqual(str(rev), expected)

    def test_save_method(self):
        """Test to check if save method works properly"""
        rev = Review()
        old_save = rev.updated_at
        rev.save()
        self.assertNotEqual(old_save, rev.updated_at)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict_method(self):
        """Test to check if to_dict method works properly"""
        rev = Review()
        expected = {
            "id": rev.id,
            "__class__": "Review",
            "created_at": rev.created_at.isoformat(),
            "updated_at": rev.updated_at.isoformat()}
        self.assertDictEqual(rev.to_dict(), expected)