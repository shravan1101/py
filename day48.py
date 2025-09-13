x = 10


def fuctions():
    global x
    x = 12
    y = 11
    print(y)  # this is a local variable
    print(x)


print(x)  
fuctions()

# print(y)
