#!/usr/bin/python
n=input("The user value is: ")
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print("it is not prime number")
            break
    else:
        print("it is prime")
else:
    print("enter more number")
