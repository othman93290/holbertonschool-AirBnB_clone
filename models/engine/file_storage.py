import os
import json

class FileStorage:
    def __init__(self):
        self.__file_path = 'file_storage.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    new_instance = obj_class(**value)
                    self.__objects[key] = new_instance

# Reloading the saved instance
new_file_storage = FileStorage()
new_file_storage.reload()
print(new_file_storage.all())
