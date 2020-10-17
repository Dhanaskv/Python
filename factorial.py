#!/usr/bin/python
def fun(var):
    if (var<0):
        return 0
    elif(var == 0 or var == 1):
        return 1
    else:
        fact=1
        while(var>1):

            fact=fact*var
            var=var-1
        return fact



var =0
print ("The factorial is : ", fun(var))






