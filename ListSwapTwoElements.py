#!/usr/bin/python
L1=[10,20,30,40,50,60,70]
pos1=2
pos2=5
temp=L1[pos1-1]
L1[pos1-1]=L1[pos2-1]
L1[pos2-1]=temp
print(L1)

