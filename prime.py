#!/usr/bin/python
var=input("The input value is : ")
for x in range(2,var):
    if(var%x == 0):
        print("this is non-prime")
        break


