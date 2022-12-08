

import numpy as np

from pathlib import Path

data = '\day5.txt'
path = Path.cwd()
path = str(path) + data

path_stack = str(Path.cwd()) + '\day5-stack.txt'

data = np.loadtxt(path,dtype=str)
#Only keep the numbers
data = data[:,1::2]
instructions = data.astype(int)




def parse_stack(file_name):
    stack = None
    data = open(file_name, "r")
    for d in data:
        if stack is None:
            stack = []
            #Create rows for stack
            for i in range(len(d[1::4])):
                stack.append([])

        for i in range(len(d[1::4])):
            char = d[(4*i+1)]
            if char != ' ':
                try:
                    #Try to turn charcter into an int if it fails it is a letter
                    int(char)
                    pass
                except:
                    stack[i].insert(0,char)
    
    data.close()
    return(stack)

stack = parse_stack(path_stack)
print(stack)
stack2 = parse_stack(path_stack)

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


for instruction in instructions:
    amount = instruction[0]
    from_ = instruction[1] - 1
    to_ = instruction[2] -1
    stack = move_stack(stack,amount, from_, to_)
    stack2 = move_stack9001(stack2, amount, from_, to_)


for stacks in stack:
    print(stacks[-1])

print('Part2')
for stacks in stack2:
    print(stacks[-1])
    