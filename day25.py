# tuple are imutable
contories = ("spain ", "Italy", "Indian", "England", "Germany")
print(contories)
temp = list(contories)
temp.append("russia")
temp.pop(3)
temp[2] = "Finland"
contories = tuple(temp)
print(contories)


contories = ("pak", "agf", "bang")
contories2 = ("Indian", "china", "japan")
k = contories + contories2

print(k)


tuple2 = (1, 1, 2, 3, 4, 5, 3, 2, 4, 6, 2, 5, 2, 13, 67)
res = tuple2.count(2)
print(res)
lol = tuple2.index(4, 2, 8)
print(lol)
print(tuple2.index(67))  # comtinf start from 0


x = len(tuple2)
print(x)
