a = "my name is shravan!@"
print(len(a))
print(a.upper())      
print(a.lower())
print(a.rstrip("!@"))

print(a.replace("shravan", "youknow"))

# this convert the words in to list from the spaces between them
print(a.split(" "))  # list

list12 = a.split(" ")
for item in list12 :
    print(item)

heading = "introductions to js "

# capitalize fist char to uppercase and rest all lower case
print(heading.capitalize())

# center

print(heading.center(110))


# center add blank spacces
print(len(heading))
print(len(heading.center(50)))


#  count a perticular word
print(heading.count("js"))


# this check the end of the string with value
str1 = "welcome to the console !!!"
print(str1.endswith("!!!"))

str1 = "welcome to the console !!!"
print(str1.endswith("to", 4, 10))

str1 = "shravan is a honest man "
print(str1.find("is"))
print(str1.index("is"))


# A-Z , a-z , 0-9 isalnum()
print(str1.isalnum())

# A-Z , a-z isalpha()
print(str1.isalpha())

# islower
print(str1.islower())

# isprintable()

str1 = " hi what a bad day \n "
print(str1.isprintable())

# isspace only works for wide space or scapes only
str2 = "                    "
print(str2.isspace())

# istitle


str1 = "Healt Is Bad"
print(str1.istitle())


# startwith("sos")
print(str1.startswith("H"))


# swapcase it convert upper case to lower nd lower to upper
print(str1.swapcase())


# title() covert the upper case of eash starting letter
str3 = " my name is sos ans so i live in sos ans so im am sos years old34"
print(str3.title())
