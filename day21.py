# def average(a, b=1): a is required arrgument
def average(a=9, b=1):
    print("the average of two number", (a + b) / 2)


average()
average(4, 2)


def name(fname, mname="jonh", lname="washinton"):
    print("kello", fname, mname, lname)


name("shravan")
name("shravan", "sachin ", "bhise")

average(b=32, a=23)  # order dosent matter


def big(*number):
    print(type(number))
    print(number)
    sum = 0
    for item in number:
        sum = sum + item
    print("average is = ", sum / len(number))


def bigg(*number):
    print(type(number))
    print(number)
    sum = 0
    for item in number:
        sum = sum + item
    return sum / len(number)


big(1, 1, 1)
print("look hare")
cv = bigg(1, 2, 3, 34)
print(cv)


def name(**name):
    print("hello ", name["fname"], name["mname"], name["lname"])


name(fname="shravan", mname="sachin ", lname="bhise")
