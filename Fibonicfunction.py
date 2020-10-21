#1/usr/bin/python
def func(var):
    a=0
    b=1
    if (var<0):
        print("This is not fibonic number")
    elif(var == 0):
        return a
    elif(var == 1):
        return b
    else:
        for x in range(2,var):
            c = a+b
            a = b
            b = c
            print(b)
        return b
print("The fibonic value is : " ,func(9))
        





