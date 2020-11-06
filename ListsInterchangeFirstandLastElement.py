#!/usr/bin/python
L1=[10,20,30,100,300,400]
print("The Original list is: ",L1)
n=len(L1)
temp=L1[0]
L1[0]=L1[n-1]
L1[n-1]=temp
print("Changing the first and last element: ",L1)
