class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def area(self):
        return self.__height * self.__width


rec1 = Rectangle(20, 10)
# rec2 = Rectangle(float(input("Enter a number two numbers: ")))
print(rec1.area())
# print(rec1.height * rec1.__width)


class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        self.__c;
        print(self.__c)
        self.__private_method()

    def __private_method(self):
        print('private')


hello = Hello('name')
print(hello.a)
print(hello._b)
# print(hello.__c)
hello.public_method()

