#!/usr/bin/python
# def counter():
#     x = 0
#     while x < 10:
#         print(x)
#         x += 1

# counter()
# class Calc():
#     def __init__(self, width,length):
#         self.width = width
#         self.length = length

#     def count(self):
#         return self.width * self.length
    
# a = int(input("Enter the width : "))
# b = int(input("Enter the length: "))
# ret = Calc(a, b)
# print(ret.count())

# calculate area of a circle 
class Area():
    def __init__(self, radius, pie):
        self.radius = radius
        self.pie = pie

    def calac(self):
        return self.pie * self.radius


a = int(input("Enter the radius : "))
b = int(input("Enter pie        : "))
ret = Area(a, b)
print(ret.calac())


def divide(x, y):
    return x/y
print(divide(14, 7))



















