import uuid
from datetime import datetime

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
        self.id = str(uuid.uuid4()).split("-")[0]  # Using only first part of UUID
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Method to return formatted string"""
        return "[{}] ({})".format(self.__class__.__name__, self.id)

    def save(self):
        """Method to update the attribute updated_at to the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method to return a dictionary that contains all keys/values"""
        obj_dict = {
            "id": self.id,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "__class__": self.__class__.__name__
        }
        return obj_dict
