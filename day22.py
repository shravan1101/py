l = [1, 2, 3, "shraavn", True]
print(l)
print(type(l))
print(l[0])

print(l[-3])
print(l[len(l) - 3])


if 7 in l:  # "6" -> no
    print("yes")
else:
    print("no")

# same thing applys for string also
if "shr" in "shravan":
    print("yes")

print(l)
print(l[:])
# print(l[0 : len(l)])
print(l[1:4])
print(l[1:4:2])  # it jump 1 ,2


# list comprehensions

list = [i for i in range(4)]
print(list)


list = [i * i for i in range(10)]
print(list)


list = [i * i for i in range(10) if i % 2 == 0]
print(list)
