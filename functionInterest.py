#!/usr/bin/python
def simple_interest(p,t,r):
    return (p*t*r)/100
p=float(input("The principal amount is:"))
t=float(input("The Rate of interest is:"))
r=float(input("The Time of years is:"))
print("The simple interest is:",simple_interest(p,t,r))

