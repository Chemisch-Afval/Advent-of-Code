import numpy as np

from pathlib import Path

data = '\day2.txt'
path = Path.cwd()
path = str(path) + data

data = np.loadtxt(path, dtype=str)

#Part 1
score = 0
#A,X = rock, B,Y = paper, C,Z = scissors
for round_ in  data:
    opp = round_[0]
    me = round_[1]
    
    if opp == 'A':
        if me == 'X':
            score += 3 + 1
        elif me == 'Y':
            score += 6 + 2
        else:
            score += 3
        
    elif opp == 'B':
        if me == 'X':
            score += 0 + 1
        elif me == 'Y':
            score += 3 + 2
        else:
            score += 6 + 3
    
    else:
        if me == 'X':
            score += 6 + 1
        elif me == 'Y':
            score += 0 + 2
        else:
            score += 3 + 3
        
    
print(score)

# Part 2
score = 0
#A = rock, B = paper, C = scissors
#X = lose, Y = Draw, Z = win
for round_ in  data:
    opp = round_[0]
    me = round_[1]
    
    if me == 'X':
        if opp == 'A':
            score += 3
        elif opp == 'B':
            score += 1
        else:
            score += 2
        
    elif me == 'Y':
        if opp == 'A':
            score += 3 + 1
        elif opp == 'B':
            score += 3 + 2
        else:
            score += 3 + 3
    
    else:
        if opp == 'A':
            score += 6 + 2
        elif opp == 'B':
            score += 6 + 3
        else:
            score += 6 + 1
            
print(score)