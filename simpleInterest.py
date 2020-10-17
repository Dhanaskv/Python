#!/usr/bin/python
def functioNname(prinAmount,rate,time):
    return (prinAmount*rate*time)/100

p=int(input("The principle amount is :"))
r=float(input("The rate is interest is :"))        
t=float(input("The time of periods is :"))
print("The simple interest is : ",functioNname(p,r,t))    
