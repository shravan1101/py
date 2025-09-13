import os

# os.rename("cultter_folder/file.txt", "cultter_folder/name.txt")

files = os.listdir("cultter_folder")
i = 0
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"cultter_folder/{file}", f"cultter_folder/{i}.png")
        i = i + 1
