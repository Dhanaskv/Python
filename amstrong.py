#!/usr/bin/python
value=0
finalSum=0
var=input("The input value is : ")
var1=var
var2=var
while(var>0):
    var=var/10
    value=value+1
print("the iteration count is : ",value)    

while(var1>0):
    newvr=var1%10
    var1=var1/10

    each_value=1
    for i in range(0,value):
        each_value=each_value*newvr

    finalSum=finalSum+each_value
if(var2 == finalSum):
    print("yes")
else:
    print("no")
    
    
     


























