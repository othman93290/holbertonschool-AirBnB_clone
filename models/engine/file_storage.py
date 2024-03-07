#!/usr/bin/python3
"""Module for FileStorage class"""
from os import path
import json


class FileStorage:
    """
    Description: FileStorage class that serializes instances to
    a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): dictionary for storing objects (class name.id)

    Methods:
        all: return the dictionary __objects
        new: set in __objects the obj with key <obj class name>.id
        save: serialize __objects (__objects -> JSON)
        reload: deserialize the JSON file to __objects (JSON -> __objects)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return all of the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Method to set in __objects the given object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj
                    in self.__objects.items()}
        with open(self.__file_path, "w") as newfile:
            json.dump(obj_dict, newfile)

    def reload(self):
        """Method to deserialize the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                for value in json.loads(file.read()).values():
                    eval(value["__class__"])(**value)