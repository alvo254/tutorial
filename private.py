class Car:
    def __init__(self, name):
        self.name = name
        self.a = 10  # publice member variable
        self._b = 20
        self.__c = 30   # private convention attribute cannot be used outside the class
        self.color = 'red'  # need not be initialized can be accessed statically

    def public_method(self):
        # print(self.a)
        print(self.__c)
        print('public')
        self.__private_method()   # accessing the private methods

    def __private_method(self):
        print('private')


ferrari = Car('jets')
print(ferrari.name)

helo = Car('alvin')
print(helo.color)
print(helo.a)
print(helo._b)
#print(helo.__c)
helo.public_method()


