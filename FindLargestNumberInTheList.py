#!/usr/bin/python
L1=[100,25,1000,34,200,5000,10000]
var=L1[0]
for i in L1:
    if i>var:
        var=i
print("The maximum element is : ",var)
print("Using another method")
print(max(L1))
print("Using another method")
n=len(L1)
L1.sort()
print(L1[n-1])
        
