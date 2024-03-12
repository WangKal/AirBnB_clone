#!/usr/bin/python3
"""Defines a class User """
from models.base_model import BaseModel


class User(BaseModel):
	""" Class of User definition
		Attrributes:
		email (string): email
		password (string) : user password
		firstname (string) : user first name
		lastname (string) : user last name
	"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """New instances of User.
        """
        super().__init__(*args, **kwargs)
