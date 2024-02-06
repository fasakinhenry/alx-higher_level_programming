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

    def to_json(self, attrs=None):
        if (isinstance(attrs, list)
           and all(type(ele) == str for ele in attrs)):
            attributes = {}
            for attribute_name in attrs:
                if (hasattr(self, attribute_name)):
                    attribute_value = getattr(self, attribute_name)
                    attributes[attribute_name] = attribute_value
            return attributes
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for keys, values in json.items():
            setattr(self, keys, values)
