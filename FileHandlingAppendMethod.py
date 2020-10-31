#!/usr/bin/python
x=open("test.txt","a")
x.write("python is interpreter language")
x.close()

x=open("test.txt","r")
print(x.read())
