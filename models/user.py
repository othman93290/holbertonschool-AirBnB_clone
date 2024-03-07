#!/usr/bin/python3
"""Module for User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Description:
        Class that defines user attributes.

    Attributes:
        email: user's email
        password: user's password
        first_name: user's first name
        last_name: user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""