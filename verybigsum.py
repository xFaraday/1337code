#!/bin/python3
#
#Given two inputs:
#1st defines how many numbers, the 2nd the
#numbers to add
#
#Example:
#Input:
#5
#1003 1004 1005 1006 1007
#Output:
#5025


tot = int(input())
ar = list(map(int, input().rstrip().split()))
store = 0

for i in range(0, tot):
    store += ar[i]

print(store)
    