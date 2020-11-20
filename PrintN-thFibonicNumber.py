#!/usr/bin/python
n=int(input("the user input is: "))
count=2
n1=0
n2=1
if n == 1:
    print('0')
elif n == 2:
    print('1')
else:
    while(count<n):
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1
    print(n2)


