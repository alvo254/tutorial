#!/usr/bin/python3
'''super function in python that allows you to reffer to you superclass in inheritance'''


class Parent:
    def __init__(self, name):
        print('parent __init__', name)


class Child(Parent):
    def __init__(self):
        print('child __init__')
        super(Child, self).__init__('Alvin')          # super().__inti__ means were calling the name in the super class
        super().__init__('max')


child = Child()
print(Child.__mro__)  # method resolution order this is the order in which methods are called
# children = Parent("alvin")
# print(children)
# rules used in mro is methods in the subclass are called first
