#!/usr/bin/python
L1=[12,31,43,23,19,2]
for i in L1:
    if i%2 != 0:
        print("the odd number is: ",i)
print("Using another method")
i=0
while(i<len(L1)):
    if L1[i]%2 != 0:
        print(L1[i])
    i=i+1
