# marks = [12, 13, 14, 15, 16, 17, 18]

# Index = 0
# for mark in marks:
#     print(mark)
#     if Index == 4:
#         print("good")
#     Index += 1

marks = [12, 13, 14, 15, 16, 17, 18]
for index, mark in enumerate(marks, 2):
    print(mark)
    if index == 2:
        print("two index")
