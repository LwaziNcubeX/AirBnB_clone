#!/usr/bin/python3
"""A User Class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class BaseModel that defines all common attributes/methods

    Attributes:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    Methods:
        __init__(self, *args, **kwargs):
            User Class Constructor
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        User Class Constructor

        Args:
            self:
            args:
            Kwargs
        """
        super().__init__(*args, **kwargs)
