string = input("enter ")
words = string.split(" ")
code = int(input("codeing 1 and decoodeing 0"))
code = True if code == 1 else False

if code:
    nword = []
    for word in words:
        if len(words) >= 3:
            r1 = "tuji"
            r2 = "sds"
            new_string = r1 + word[1:] + word[0] + r2
            nword.append(new_string)
    else:
        nword.append(word[::-1])
    print(" ".join(nword))

else:
    nword = []
    for word in words:
        if len(words) >= 3:

            new_string = word[4:-3]

            if len(new_string) > 0:
                new_string = new_string[-1] + new_string[:-1]
                nword.append(new_string)
            else:
                nword.append("")

        else:
            nword.append(word[::-1])
    print(" ".join(nword))
