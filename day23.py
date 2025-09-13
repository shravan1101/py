l = [11, 45, 7, 2, 4, 6, 1]
print(l)
# l.append(34)
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))  # it give the index
# print(l.count(6))
# print(l)

# m = l
# m[0] = 0  # this change the orginal list (l) insted of
# print(l)

# m = l.copy()


l.insert(1, 323)  # it will shit the number to the left then it will add your number
print(l)

z = ["shravan", "sachin", "bhise"]
l.extend(z)  # it well glue the or join the list at the end of the list
print(l)

k = l + z  # it well merage the two list
print(k)
