#!/usr/bin/python3
"""A program that uses the cmd module"""
import cmd

import models.base_model
from models import storage
from models.base_model import BaseModel


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
            model = eval(arg)()
            model.save()
            print(model.id)
        except NameError:
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

        if class_name != models.base_model.BaseModel.__name__:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        instance_key = f"{class_name}.{instance_id}"
        instance = storage.all().get(instance_key)

        if not instance:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        The change is saved into the JSON file.

        :param arg:
        :return:
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name != models.base_model.BaseModel.__name__:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        instance_key = f"{class_name}.{instance_id}"
        instance = storage.all().get(instance_key)

        if not instance:
            print("** no instance found **")
            return
        else:
            storage.all().pop(instance_key)

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
            model = storage.all()
            data = []
            for obj_id in model.keys():
                obj = model[obj_id]
                data.append(str(obj))

            result = '["' + '", "'.join(data) + '"]'
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
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name != models.base_model.BaseModel.__name__:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        instance_key = f"{class_name}.{instance_id}"
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
        attribute_value = args[3]
        key = "{}.{}".format(class_name, instance_id)
        data = storage.all()
        new_value = ""
        for i in attribute_value:
            if i == '\"':
                continue
            else:
                new_value += i

        obj = data[key]
        setattr(obj, attribute_name, new_value)

        data[key] = obj
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
