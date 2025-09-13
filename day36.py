# a = int(input("enter a number : "))

# print(f"Multiplications table of {a} is : ")

# try:
#     for i in range(1, 11):
#         print(f" {a} X {i} = {a*i}")
# except Exception as e:
#     print(e)

# print("some imp line of code")
# print("end of the programe")


# a = input("enter a number : ")+

# print(f"Multiplications table of {a} is : ")

# try:
#     for i in range(1, 11):
#         print(f" {int(a)} X {i} = {int(a)*i}")
# except:
#     print("invalid input ")

# print("some imp line of code")
# print("end of the programe")


try:
    num = int(input("enter a number"))
    a = [1, 2]
    print(a[num])
except ValueError:
    print("the value recive is not a integer")
except IndexError:
    print("index erro")
