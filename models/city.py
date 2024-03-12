#!/usr/bin/python3
"""Defines a class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines City.

    Attributes:
        name (string): name of city.
        state_id (string): id of state.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """New instances of City.
        """
        super().__init__(*args, **kwargs)
