#!/usr/bin/python
Fibonic=input("The user input value is :")
a=0
b=1
if (Fibonic<0):
    print("This is incorrect value")
elif (Fibonic == 0):
    print("0 is the fibonic number value")
elif (Fibonic == 1):
    print("1 is the fibonic number value")
else:
    for i in range(2,Fibonic):
        c = a+b
        a = b
        b = c

    print("The Fibonic value is : ",b)
