#!/usr/bin/python3
"""Module for Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Description:
        Class that defines review attributes.

    Attributes:
        place_id: place's id
        user_id: user's id
        text: review's text
    """
    place_id = ""
    user_id = ""
    text = ""