import os


for i in range(0, 100):
    os.rename(f"dats/good{i+1}", f"dats/days{i+1}")
