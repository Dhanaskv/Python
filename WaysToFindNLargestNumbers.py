#!/usr/bin/python
L1=[10,20,30,40,50]
L2=[]
N=2
for i in range(0,N):
    mx=0
    for i in range(0,len(L1)):
            if L1[i]>mx:
                mx=L1[i]
    L1.remove(mx)
    L2.append(mx)
print("The value is: ",L2)


