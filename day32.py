# # s1 = {1,2,5,6}
# # s2 = { 3,6,7}

# # print(s1.union(s2)) # print the union of two. sets
# # s1.update(s2) # it take the uncoom part of s2 in s1
# # print(s1,s2)


# # union ()
# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities3 = cities.union(cities2)
# # print(cities3)


# # update ()
# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities.update(cities2) # cities getupdate with city 2
# # print(cities)

# #  intersection and intersection_update():

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities3 = cities.intersection(cities2)
# # print(cities3)

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities.intersection_update(cities2) # the common between city 1 and city 2 get transfer in city 1
# # print(cities)


# #  symmetric_difference and symmetric_difference_update():
# #   for_ mulla = (AUB) - (A∩B)

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities3 = cities.symmetric_difference(cities2)
# # print(cities3)

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities.symmetric_difference_update(cities2)
# # print(cities)


# # difference() and difference_update():

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Seoul", "Kabul", "Delhi"}
# # cities3 = cities.difference(cities2)  # print the item presnt in the parent set
# # print(cities3) #  now here delhi is in both. set but it will not print

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Seoul", "Kabul", "Delhi"}
# # print(cities.difference(cities2))

# # isdisjoint():

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # print(cities.isdisjoint(cities2))

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Seoul", "Kabul"}
# # print(cities.issuperset(cities2))
# # cities3 = {"Seoul", "Madrid","Kabul"}
# # print(cities.issuperset(cities3))

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi" ,"Seoul" , "Kabul"}
# # cities2 = {"Seoul", "Kabul"}
# # print(cities.issuperset(cities2))
# # cities3 = {"Seoul", "Madrid","Kabul"}
# # print(cities.issuperset(cities3))


# Chats
# Archived
# New Chat
# just now
# New chat with Assistant
# Assistant answers questions, refines code, and makes precise edits.
# Assistant mode

# advanced
# Claude 4.0 Sonnet

# Ask Assistant, use @ to include specific files...
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))
# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")
# Set Methods
# There are several in-built methods used for the manipulation of set.They are explained below

# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

# Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))
# Output:
# False

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

# Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))
# Output:
# False
# False

# issubset():

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))


# add()
# If you want to add a single item to the set use the add() method.

# Example:
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# update()
# it is use whrn adding one than more item to a set

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2) # cities get update by cities 2
# print(cities)


# remove()/discard()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")  # it will throw a error when the item is not found
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("shravan")  # it will throw a error when the item is not found
print(cities)
# pop()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)


# del

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities # entire set is deleted which mean it is not define
# print(cities)

# clear():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")