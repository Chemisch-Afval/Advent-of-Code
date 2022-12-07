
import numpy as np

from pathlib import Path

data = '\day4.txt'
path = Path.cwd()
path = str(path) + data

data = np.loadtxt(path,dtype=str)

#data = np.array(['2-4,6-8',
#'2-3,4-5',
#'5-7,7-9',
#'2-8,3-7',
#'6-6,4-6',
#'2-6,4-8'])

#Preprocess
enclosed = 0
enclosed_2 = 0
for i,d in enumerate(data):
    d = d.split('-')
    elf_1l = int(d[0])
    d_2 = d[1].split(',')
    elf_1u = int(d_2[0])
    elf_2l = int(d_2[1])
    elf_2u = int(d[-1])
    
    diff_l = elf_1l-elf_2l
    diff_u = -elf_1u + elf_2u
    metric = diff_l * diff_u
    #print(diff_l,diff_u , ':', elf_1l,elf_1u,elf_2l,elf_2u)
    if metric >= 0:
        enclosed+= 1
        #enclosed_2 += 1
    
    if (elf_1u >= elf_2l and elf_1u <= elf_2u) or (elf_1l <= elf_2u and elf_1l >= elf_2l):
        enclosed_2 += 1
    elif (elf_2u >= elf_1l and elf_2u <= elf_1u) or (elf_2l <= elf_1u and elf_2l >= elf_1l):
        enclosed_2 += 1
    
            
print(enclosed)
print(enclosed_2)
    
    