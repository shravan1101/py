class math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def adt(a, b):
        return a + b  # you can add this with out using self


# resukt = math.add(1, 2)
# print(resukt)  # out put three

a = math(5)
print(a.num)


a.addtonum(4)
print(a.num)


print(math.adt(12, 10))
print(a.adt(12, 10))
