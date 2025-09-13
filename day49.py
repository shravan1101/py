f = open("my_file.txt", "r")
# print(f)


txt = f.read()
print(txt)
f.close()


with open("my_file12", "a") as r:
    r.write("lets go")
