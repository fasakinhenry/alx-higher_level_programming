#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute


class MyClass():
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name) # type: ignore

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name) # type: ignore
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
