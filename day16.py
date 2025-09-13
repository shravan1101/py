x = int(input("enter a number"))

match x:
    case 0:
        print("zero")

    case 4:
        print("case four")

    case _ if x != 90:
        print(x, "is not 90")
    case _ if x != 80:
        print(x, "is not 80")
    case _:  # default case
        print(x, "is not 70")

