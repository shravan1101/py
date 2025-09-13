# map


# def cube(x):
#     return x * x * x


# print(cube(2))
lists = [1, 2, 3, 4, 5, 6]

# new_list = []

# for num in list:
#     new_list.append(cube(num))

new_list = list((map(lambda x: x * x * x, lists)))
# it takes the fuctions and the list and iterate the index to send to functions

print(lists)
print(new_list)


# Fliter
def filter_functio(a):
    return a > 4


new2_l = list(filter(filter_functio, lists))
print(lists)
print(new2_l)


# reduce

from functools import reduce

number = [1, 2, 3, 4, 54, 65, 12.0]

sum = reduce(lambda x, y: x + y, number)

print(sum) 
