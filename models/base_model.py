#!/usr/bin/python3
""" The base model """
import uuid
import datetime

class BaseModel:
    """ The base model class"""
    def __init__(self):
        """ Initialize """
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime
        self.updated_at = datetime.datetime

    def __str__(self):
        """ to string """
        pass

    def save(self):
        """ updates updated_at value """
        self.updated_at = datetime.datetime
    
    def to_dict(self):

