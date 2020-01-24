from functools import reduce
# def add(x, y):
#     return x + y

add = lambda x, y : x + y
print(add(4, 5))

my_list = [2, 5, 4, 6, 8, 9]
my_list2 = [3, 5, 3, 2, 5, 8]

a = map(lambda x: x * 2, my_list)
print(list(a))

b = map(lambda x, y: x + y, my_list, my_list2)
print(list(b))

d = filter(lambda x: True if x > 5 else False, my_list)
print(list(d))

r = reduce(lambda x, y: x + y, my_list)
print(r)








