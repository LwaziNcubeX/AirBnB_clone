#!/usr/bin/python3
"""A program that uses the cmd module"""
import cmd
from models import storage
import models.base_model
from models.base_model import BaseModel
from models.user import User
import shlex
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


CLASSES = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class HBNBCommand(cmd.Cmd):
    """
    A program that uses the cmd module

    Attributes:
        prompt: custom prompt

    Methods:
        do_quit(self, arg):
            Quit command to exit the program
        do_EOF(self, arg):
            EOF command to exit the program
        help_help(self):
            Shows help information about commands
        emptyline(self):
            empty line
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_help(self):
        """Help section info about all commands"""
        print("Shows help information about commands")

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            model = CLASSES[arg]()
            model.save()
            print(model.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.

        :param arg:
        :return:
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        instance_key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(instance_key)

        if not instance:
            print("** no instance found **")
            return

        print(instance)

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.

        :param arg:
        :return:
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            data = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == arg]
            result = "[" + ", ".join(data) + "]"
            print(result)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
         by adding or updating attribute.

        :param arg:
        :return:
        """
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        instance_key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(instance_key)

        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3].strip('"')

        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        The change is saved into the JSON file.

        :param arg:
        :return:
        """
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        instance_key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(instance_key)

        if not instance:
            print("** no instance found **")
            return

        instance.delete()
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
