#!/usr/bin/python3
"""Module for BaseModel class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Description: BaseModel class that defines all common
    attributes/methods for other classes

    Attributes:
        id (str): unique id for each instance
        created_at (datetime): time of instance creation
        updated_at (datetime): time of instance update

    Methods:
        __init__: constructor for BaseModel class
        save: update the attribute updated_at to the current datetime
        to_dict: return a dictionary that contains all keys/values of __dict__
        __str__: return formatted string
    """
    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """Method to return formatted stringg"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Method to update the attribute updated_at to the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Method to return a dictionary that contains all keys/values"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict