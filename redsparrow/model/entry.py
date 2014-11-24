"""Representation of the entry(text) in DB"""
from mongoengine import *
import datetime

class LinesInText(Document):
    lines = ListField(IntField(required=True, min_value=1))
    words = ListField(IntField(required=True, min_value=1))

class Result(Document):
    id = IntField(required=True)

