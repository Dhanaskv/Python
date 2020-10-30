#!/usr/bin/python
try:
    a=input("The first value is: ")
    b=input("The second value is: ")
    c=a/b
    print(c)
except ZeroDivisionError:
    print("This is division error")
except NameError:
    print("Name is not defined")



