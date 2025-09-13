def func1():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("enter the index: "))
        print(l[i])
        return 1

    except:
        print("not working")
        return 0

    finally:
        print("exicuted")


x =func1()
print(x)
