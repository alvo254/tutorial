#!/usr/bin/python
import math

def demo(self, a, b, c):
    d = sqrt(b**2 - 4*a*c)
    root1 = (-b+d)/(2*a)
    root2 = (b+d)/(2*a)
    print(root1, root2)
    print('SE')



# import math
# r = float(input('Enter the radius: '))
# area = math.pi * r * r
# print("Area of the circle is: %.2f"%area)

PI = 3.142
radius = float(input("Enter the radius: "))
area = PI * radius * radius
circumference = 2 * PI * radius
print("Area of circle = %.2f" %area)
print("circumference of a circle = %.2f" %circumference)
