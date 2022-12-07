

import numpy as np

from pathlib import Path

data = '\day5.txt'
path = Path.cwd()
path = str(path) + data

data = np.loadtxt(path,dtype=str)
#Only keep the numbers
data = data[:,1::2]
instructions = data.astype(int)



def move_stack(stack,amount, from_, to_):
    for i in range(amount):
        move = stack[from_][-1]
        stack[to_].append(move)
        stack[from_] = stack[from_][:-1]
        
    return(stack)

def move_stack9001(stack, amount, from_, to_):
    move = stack[from_][-amount:]
    for item in move:
        stack[to_].append(item)
    stack[from_] = stack[from_][:-amount]
    return(stack)

stack = [['W','M','L','F'],
        ['B', 'Z', 'V', 'M', 'F'],
        ['H','V','R', 'S','L','Q'],
        ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
        ['L', 'S', 'W'],
        ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
        ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
        ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
        ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']]

stack2 = [['W','M','L','F'],
          ['B', 'Z', 'V', 'M', 'F'],
          ['H','V','R', 'S','L','Q'],
          ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
          ['L', 'S', 'W'],
          ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
          ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
          ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
          ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']]

for instruction in instructions:
    amount = instruction[0]
    from_ = instruction[1] - 1
    to_ = instruction[2] -1
    stack = move_stack(stack,amount, from_, to_)
    stack2 = move_stack9001(stack2, amount, from_, to_)

print(stack)

for stacks in stack:
    print(stacks[-1])

print('Part2')
for stacks in stack2:
    print(stacks[-1])
    