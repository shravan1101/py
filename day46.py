import os


if(not os.path.exists("dats")):
    os.mkdir("dats")
    
for i in range(0 ,100):
    os.mkdir(f"dats/Day{i+1}") 