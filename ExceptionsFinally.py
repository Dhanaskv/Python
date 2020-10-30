#!/usr/bin/python
try:
    a=input("user input value is :")
    b=input("second value is :")
    c=a/b
    print(c)
except ZeroDivisionError:
    print("can't divide")
finally:
    print("program finished")
