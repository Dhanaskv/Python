#!/usr/bin/python
file1=open("f1.txt","a")
file1.write("python world")
file1.close()

file1=open("f1.txt","r")
print(file1.read())
