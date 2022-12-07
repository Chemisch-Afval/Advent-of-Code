import numpy as np

from pathlib import Path

data = '\day6.txt'
path = Path.cwd()
path = str(path) + data

data = np.loadtxt(path,dtype=str)
data = str(data)

#Part 1
for i in range(len(data)):
    window = data[i:i+4]
    window_ = [*set(window)]
    if len(window_) == 4:
        print(window,i+4)
        break
    
#Part 2
for i in range(len(data)):
    window = data[i:i+14]
    window_ = [*set(window)]
    if len(window_) == 14:
        print(window,i+14)
        break