#!/usr/bin/python
file1=open("file.txt","a")
file1.write("Hai dhana")
file1.close()
file1=open("file.txt","r")
print(file1.read())
