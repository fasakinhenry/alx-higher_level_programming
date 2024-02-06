#!/usr/bin/python3
"""A student class that defines a student by
Public instances attributes:
first_name, last_name, age
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
