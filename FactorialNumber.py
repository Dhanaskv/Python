#!/usr/bin/python
a=input("The user input is: ")
var=1
if a<0:
    print("please enter positive value")
elif a == 0:
    print("The Factorial value is 1")
else:
    for i in range(1,a+1):
        var=var*i
    print(var)

