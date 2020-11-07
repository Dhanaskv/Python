#!/usr/bin/python
L1=[1,2,3,4,5,6,7,8]
L1.remove(3)
print(L1)
n=input("The remove value is :")
m=input("The second remove value is: ")
for i in L1:
    if i == n:
        L1.remove(i)
    elif i == m:
        L1.remove(i)
print(L1)
