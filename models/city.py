#!/usr/bin/python3
"""Module for City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Description:
        Class that defines city attributes.

    Attributes:
        state_id: state's id
        name: city's name
    """
    state_id = ""
    name = ""