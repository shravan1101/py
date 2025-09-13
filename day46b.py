import os

folders = os.listdir("dats")

print(folders)

print("\n\n\n\n\n\n")

for folder in folders:
    # print(folder)
    print(folder)
    print(os.listdir(f"dats/{folder}"))
