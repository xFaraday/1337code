#!/bin/python3

num = int(input())
n = int(input())
arr = list(map(int, input().rstrip().split()))
c = 0
for i in range(0, n):
    if i == num:
        print(arr.index(num))
    elif c == n:
        print(arr[-1:])
    else:
        continue
    c += 1
    print(c)
