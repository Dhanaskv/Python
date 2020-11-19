#!/usr/bin/python
start=input("first: ")
end=input("second: ")
for i in range(start,end+1):
    for var in range(2,i):
        if i%var == 0:
            break
    else:
        print("it is prime")
        print(i)
