#!/usr/bin/python3
"""A class BaseModel that defines all common attributes/methods"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    A class BaseModel that defines all common attributes/methods

    Attributes:
        id: string - generated unique id using uuid.uuid4()
        created_at: datetime - datetime when an instance is created
        updated_at: datetime - datetime when an instance is updated

    Methods:
        __init__(self, *args, **kwargs):
            initializes a new instance of the class with the specified
            parameters
        save(self):
            updates the public instance attribute updated_at with the
            current datetime
        to_dict(self):
            returns a dictionary containing all keys/values of __dict__
            of the instance:
    """
    def __init__(self, *args, **kwargs):
        """
        The __init__ method initializes a new instance of the class with
        the specified parameters.

        Parameters:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            None.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string representation using dict

        param
        return: string
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attrib updated_at with the current datetime

        param
        return: Nothing
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of
        the instance

        param
        return:
        """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['id'] = self.id
        return new_dict
