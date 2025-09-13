import random


def check(comp, user):
    #  0 =   snake
    #  1 =   water
    # . 2 =   gun
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 2 and user == 0:
        return -1
    if comp == 1 and user == 2:
        return -1
    return 1


comp = random.randint(0, 2)
user = int(input("enter  0 -> snake 1 -> water 2-> gun "))

score = check(comp, user)
print("you", user)
print("computer", comp)

if score == 0:
    print("draw")

elif score == -1:
    print("you fuked up ")
else:
    print("you win")
