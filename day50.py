# f = open("my_file.txt", "r")

# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, typeof(line))
#         break

# i = 0
# with open("my_file.txt", "r") as file:
#     while True:
#         i += 1
#         line = file.readline()
#         if not line:
#             break
#         marks = line.split(",")
#         m1 = marks[0]
#         m2 = marks[1]
#         m3 = marks[2]
#         print(f"Marks of student {i} is {m1}")
#         print(f"Marks of student {i} is {m2}")
#         print(f"Marks of student {i} is {m3}")
#         print(line)

# f = open("my_file2.txt", "w")
# line = ["line1\n", "linw2\n", "linw3\n"]
# f.writelines(line)
# f.close()

f = open("my_file2.txt", "w")
lines = ["line1", "linw2", "shravan"]
for line in lines:
    f.write(line + "\n")
f.close()
