#!/user/bin/python3
"""City class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel and stores city information.

    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
