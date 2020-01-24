'''class methods are different as they are called by a class which is passed to the cls parameter of the method'''


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_lenght):
        return cls(side_lenght, side_lenght)


square = Rectangle.new_square(5)
print(square.calculate_area())


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Wooof!")


fido = Dog("Fido", "Brown")
fido.bark()


class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth * self.length

    @classmethod
    def new(cls, side):
        return cls(side, side)


a = int(input("enter length of a rectangle:"))
b = int(input("enter breadth of a rectangle:"))
obj = rectangle.new(5)
print("Area of rectangle is: ", obj.area())


'''static methods are similar to to class methods except they don't receive any additional arguments'''


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == 'pineapple':
            raise ValueError('No pineapples')
        else:
            return True


ingredients = ['cheese', 'onions', 'spam']
if all(Pizza.validate_topping()for i in ingredients):
    pizza = Pizza(ingredients)
Pizza()























