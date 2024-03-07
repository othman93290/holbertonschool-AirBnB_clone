#!/usr/bin/python3
"""Module for Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Description:
        Class that defines amenity attributes.

    Attributes:
        name: amenity's name
    """
    name = ""