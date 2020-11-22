#!/usr/bin/python
file1=open("file.txt","w")
file1.write("Hai python")
file1.close()
file1=open("file.txt","r")
print(file1.read())

