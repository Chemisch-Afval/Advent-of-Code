import numpy as np

from pathlib import Path

data = '\day2.txt'
path = Path.cwd()
path = str(path) + data

data = open(path, "r")

#Part 1
#A,X = rock, B,Y = paper, C,Z = scissors
for i, d in enumerate(data):
    print(d[2])