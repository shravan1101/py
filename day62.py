# private

# class Employee:
#     def __init__(self):
#         self.__name = "shravan"


# a = Employee()
# # print(a.__name) # cannot be accessed

# print(a._Employee__name) # can be accessed indirectly

# print(a.__dir__())


# # Protected Access Modifier


class student:
    def __init__(self):
        self._name = "shravanƒ"

    def _funName(self):  # potected methtod
        return "codewithshravan"


class Subject(student):  # inheritade class
    pass


obj = student()
obj1 = Subject()


# calling by the oject of student class
print(obj._name)
print(obj._funName)

# calling by the object of subject class
print(obj1._name)
print(obj1._funName)


print(obj1.__dir__())
