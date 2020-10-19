#!/usr/bin/python
def var(a):
    arr=0
    while(a>0):
        dgit=a%10
        arr=arr+dgit
        a=a/10
    return arr
print("The total element is :",var(153))
