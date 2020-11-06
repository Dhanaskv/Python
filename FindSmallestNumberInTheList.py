#!/usr/bin/python
L1=[30,40,2,300,4020,-1,-100]
print(min(L1))
print("Using another method")
L1.sort()
print(L1[0])
print("Using another method")
n=len(L1)
for i in range(0,n):
    if L1[i] == min(L1):
        print(min(L1))

