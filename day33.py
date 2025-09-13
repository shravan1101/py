info = {"name": "shravan", "age": 17}
print(info["name"])
print(info)
print(info.keys())
print(info.values())

# for key in info.keys():
#     print(f" the value for the following {key} is {info[key]}")


# for key in info.value():
#     print(f"the value is {key}")


print(info.items())
for key, value in info.items(): 
    print(f"the corresponding to the key {key} is {value}")
