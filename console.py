#!/usr/bin/python3
"""A program that uses the cmd module"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
