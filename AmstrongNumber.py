#!/usr/bin/python
num=input("The user input is: ")
x=len(str(num))
sum1=0
var=num
while(var>0):
    n=var%10
    sum1=sum1+n**x
    var=var/10
if sum1 == num:
    print("It is amstrong number")
else:
    print("It is not amstrong number")
