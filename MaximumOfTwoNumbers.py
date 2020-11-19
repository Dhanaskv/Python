#!/usr/bin/python
a=input("The 1st value is: ")
b=input("The 2nd value is: ")
if a>b:
    print(a)
elif b>a:
    print(b)
elif a == b:
   print("value is equal")


print("using another method")
print(max(a,b))
