import numpy as np

from pathlib import Path

data = '\day1.txt'
path = Path.cwd()
path = str(path) + data

data = open(path, "r")

#Part 1
data_per_elf = []
sum_d = 0
for i, d in enumerate(data):
    #print(i,d)
    if d != '\n':
        sum_d += int(d)
        
    else:
        data_per_elf.append(sum_d)
        sum_d = 0



print('Most calories:', np.max(data_per_elf))

#Part 2

top_three = []
data_per_elf = np.asarray(data_per_elf)

i = 0
while i < 3:
    #Append max
    top_three.append(np.max(data_per_elf))
    #remove max from array
    data_per_elf = data_per_elf[data_per_elf!=np.max(data_per_elf)]
    i+= 1
    
print('Sum of top three elves:', sum(top_three))

data.close()