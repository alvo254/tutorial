"""decorators wrap a function and modify its behaviour without changing the source code"""
import pdb


def deco_func(func):
    def wrapper_func():
        print('----------------------')
        func()
        print('----------------------')

    return wrapper_func()


def say_hello():
    print('Hello World')


helo = deco_func(say_hello)

