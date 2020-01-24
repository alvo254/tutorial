class Car:
    def __init__(self, speed, color):
        # print("the __init__ is called")
        self.__speed = speed
        self.color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


ford = Car(300, 'red')
carb = Car(200, 'blue')
carb.set_speed(310)
ford.set_speed(400)
print("fords color is  %s" % ford.color)
print(ford.get_speed())
print(carb.get_speed())



