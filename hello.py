def hello(name, title, **projects):
    print("name: ", name)
    print("Title: ", title)
    print("projects: ", projects)
    for key, value in projects.items():
        print(key, ' ', value)


hello('Alvin', 'Senior developer', kisumu='interiors', malindi='mjengo', \
      kisi='planting')

### Class and how they work ###


# class carr():
#     pass
#
#
# ford = carr()
# lambo = carr()
#
#
# ford.speed = 200
# lambo.color = 'red'
#
# print(ford.speed)

# setter and getter functions in python


class car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def set_speed(self, value):  # set method
        self.speed = value

    def get_speed(self):  # get method
        return self.speed


ford = car(200, 'red')
lexus = car(310, 'mate black')

ford.speed = 400
ford.set_speed(300)
# print(ford.get_speed())
print(ford.speed)
