import random

list = ["snake", "water", "gun"]
com = random.choice(list)

y = input("\nenetr snake water gun\n ").lower()
print(f" \t \t you {y} and computer {com}")

if com == y:
    print("draw")

if (com == "snake") and (y == "water"):
    print("losss")

if (com == "water") and (y == "snake"):
    print("win")


if (com == "gun") and (y == "water"):
    print("win")
if (com == "water") and (y == "gun"):
    print("loss")


if (com == "snake") and (y == "gun"):
    print("win")
if (com == "gun") and (y == "snake"):
    print("loss")
