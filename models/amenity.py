#!/usr/bin/python3
"""Amenity class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel and stores amenity information.

    Attributes:
        name: string - empty string
    """
    name = ""
