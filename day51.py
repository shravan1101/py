# with open("51.txt", "r") as r
#     r.seek(10)
#     man = r.read(3)
#     print(man)
#     print(r.tell())

# print(r)
# print(type(r))


with open("sample.txt", "w") as f:
    f.write("hello World")
    f.truncate(5)  # it will reduce the file size to 5


with open("sample.txt", "r") as f:
    print(f.read())
