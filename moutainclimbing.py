#!/bin/python

#Prompt:
#Given vertical direction of a hiking path determine # of valleys if valleys="DD"
#
#Example input: DDUDUDUDDUUDD
#Example output: 3

#range=int(input())
steps=input()

listwor = list(steps)
print(listwor)
print(listwor.count('D'))

def inputcheck(listwor):
    if (listwor.count('D')<=1):
        print("no valleys")
        exit
    else:
        print("Valleys are most likely present")
        valleycount(listwor)
        exit

def valleycount(listwor):
    indices = [i for i, x in enumerate(listwor) if x == "D"]
    a=1
    vc=0
    print(indices)
    print(indices[a])
    for i in indices:
        if (indices[a]-i==1):
            if (a>len(indices)): 
                break
            vc+=1
            a+=1
        else:
            if (a>len(indices)): 
                break
            a+=1
    print(vc)
        
            

inputcheck(listwor)
    