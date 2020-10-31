#!/usr/bin/python
x=open("test.txt","w")
x.write("python is most using in world")
x.close()

x=open("test.txt","r")
print(x.read())
