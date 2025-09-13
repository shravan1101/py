ep1 = {122: 45, 123: 56, 456: 12}
ep2 = {222: 67, 5666: 12}

ep1.update(ep2)
# ep1.clear()
print(ep1)
# empty = {}
ep1.pop(122)
print(ep1)
ep1.popitem()
print(ep1)
# del ep1 # it will deleat all the dictionary 
# del ep1[122]

