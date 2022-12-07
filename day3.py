import numpy as np
import re
from pathlib import Path

data = '\day3.txt'
path = Path.cwd()
path = str(path) + data

data = np.loadtxt(path, dtype=str)

#data = np.array(['vJrwpWtwJgWrhcsFMMfFFhFp',
#'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#'PmmdzqPrVvPwwTWBwg'])

def fill_missing(list_,fill):
    if len(list_) == list_[-1]:
        return(list_)
    else:
        num = list_[0]
        i = -1
    
        while num < list_[-1]:
            num += 1
            i += 1
    
            if num in list_: continue
    
            if i < len(list_) - 1:
                list_.insert(i + 1, fill)
            else:
                list_.append(fill)
        
        for i in range(list_[0]-1):
            list_.insert(0,fill)
        for i in range(52-list_[-1]):
            list_.append(fill)
        return(list_)
    
compartments = []
sum_ = 0
for d in data:
    half = int(len(d)/2)
    string1 = d[:half]


    list1 = [ord(char) -96 for char in string1]
    list1 = np.asarray(list1)
    list1[list1<0] += 58
    list1 = [*set(list1)]
    list1 = sorted(list1)
    list1 = fill_missing(list1,-1)
    
    #Get all characters that occur more than once
    #string1 = ''.join(string1)
    
    string2 = d[half:]
    string2 = sorted(d[half:])

    list2 = sorted([ord(char) -96 for char in string2])
    list2 = np.asarray(list2)
    list2[list2<0] += 58

    list2 = [*set(list2)]
    list2 = sorted(list2)
    list2 = fill_missing(list2,-2)
        
    list1 = np.asarray(list1)
    list2 = np.asarray(list2)
    
    sum_ += sum(list1[list2-list1==0])
    compartments.append([list1,list2-list1])

print(sum_)
compartments = np.asarray(compartments)

#Part 2
groups = []
sub = []
sum_2 = 0
for i, d in enumerate(data):
    list1 = [ord(char) -96 for char in d]
    list1 = np.asarray(list1)
    list1[list1<0] += 58
    list1 = [*set(list1)]
    list1 = sorted(list1)
    list1 = fill_missing(list1,-(i+1)**i)
    sub.append(list1)
    if len(sub)>= 3:
        sub = np.asarray(sub)
        common_1 = sub[0] - sub[1]
        common_2 = sub[1] - sub[2]
        common = common_1 - common_2
        sum_2 += sub[0][common==0][0]
        
        sub = []
        
print(sum_2)



