#!/usr/bin/python3
""" The base model """
import uuid
import datetime

class BaseModel:
    """ The base model class"""
    def __init__(self):
        """ Initialize """
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ to string """
        return "[{}] ({}) {}".format(self.__class__.__name__, str(self.id), self.__dict__)

    def save(self):
        """ updates updated_at value """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ to dictionary """
        rdict = self.__dict__.copy()
        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        rdict['__class__'] = self.__class__.__name__
        
        return rdict
