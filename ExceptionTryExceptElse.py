#!/usr/bin/python
try:
    a=input("The first value is: ")
    b=input("The second value is : ")
    c=a/b
    print(c)
except ZeroDivisionError:
    print("can't divide")
else:
    print("The else statement is executed")

