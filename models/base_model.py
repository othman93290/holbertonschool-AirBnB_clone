import json
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
        }

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.to_dict()))

    def save(self):
        self.updated_at = datetime.now()
    
    @classmethod
    def from_dict(cls, data_dict):
        instance = cls()
        for key, value in data_dict.items():
            setattr(instance, key, value)
        return instance

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        data_dict = json.loads(json_str)
        return cls.from_dict(data_dict)
