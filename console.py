#!/usr/bin/python3
"""Module for HBNBCommand class"""
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
"""Comments"""


class HBNBCommand(cmd.Cmd):
    """Class for the console"""

    prompt = "(hbnb) "

    class_list = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End Of File command to exit the program (ctrl + D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """
            Creates a new instance of the specified class,
            saves it, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.class_list:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an
        instance based on class name and id."""
        tokens = arg.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance (save the change into the JSON file)"""
        tokens = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if tokens[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(tokens[0], tokens[1])
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return
            else:
                del (objects[key])
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        object_list = []
        objects = storage.all()

        if not arg:
            for key, values in objects.items():
                object_list.append(str(values))
            print(object_list)
            return
        elif arg in self.class_list:
            for keys, values in objects.items():
                object_list.append(str(values))
            print(object_list)
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        """
        tokens = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if tokens[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(tokens) < 3:
            print("** attribute name missing **")
            return
        if len(tokens) < 4:
            print("** value missing **")
            return
        instance = storage.all()[key]
        attribute_name = tokens[2]
        attribute_value = tokens[3].strip('"').replace('"', '')
        setattr(instance, attribute_name, attribute_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()