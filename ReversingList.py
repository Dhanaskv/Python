#!/usr/bin/python
L1=[10,20,"python","word",40]
L2=[]
n=len(L1)
for i in range(n-1,0,-1):
    L2.append(L1[i])
print(L2)
print("Using another method")
m=[1,2,3,4,5,6]
n=[]
j=len(m)-1
while(j>=0):
    n.append(m[j])
    j=j-1
print(n)    



