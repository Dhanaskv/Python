#!/usr/bin/python
var1=input("the 1st value is :")
var2=input("the 2st value is :")
for x in range(var1,var2):
     for y in range(2,x):
         if(x%y == 0):
             print("the value is non- prime",x)
             break
