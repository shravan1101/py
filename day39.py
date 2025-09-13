questions = [
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
    ["how is shravan", "good", "mucle boy", "sexy", "all of they a above", 4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\n questions for RS. {levels[i]}")
    print(f" a. {question[1]}\t\t b. {question[2]}")
    print(f" a. {question[3]}\t\t b. {question[4]}")
    reply = int(input("1 -4 choss or 0 to quit "))

    if reply == 0:
        money = levels[i - 1]
        break
    if reply == question[-1]:
        print(f"aaazada money {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("wonf ans")
        break
print(f"you take this much {money}")
