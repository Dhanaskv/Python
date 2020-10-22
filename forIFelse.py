#!/usr/bin/python
arr=[1,2,3,4,5,6]
n=input("User input value is :")
sum1=0
for i in range(0,6):
    if (n == arr[i]):
        sum1=1
        break
if (sum1 == 1):
    print("true")
else:
    print("false")


