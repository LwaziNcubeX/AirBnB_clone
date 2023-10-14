#!/usr/bin/python3
"""A User Class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User that inherits from base model

    Attributes:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
