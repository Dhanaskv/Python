#!/usr/bin/python
value=0
var=input("The variable value is: " )
while(var>0):
    alpha=var%10
    var=var/10
    value=value+1
print("The value count is: ",value)  


