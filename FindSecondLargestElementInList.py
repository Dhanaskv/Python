#!/usr/bin/python
L1=[100,200,120,300,400,500,600,7000,800]
L1.sort()
print("The second largest value is: ",L1[-2])
mx=max(L1[0],L1[1])
secondmx=min(L1[0],L1[1])
n=len(L1)

for i in range(2,n):
    if L1[i]>mx:
        secondmx=mx
        mx=L1[i]
    elif L1[i]>secondmx:
        mx != L1[i]
        secondmx=L1[i]
print("The second maximum value is: ",secondmx)
