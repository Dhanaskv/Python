#!/bin/python
count=0
n=input("the user input is: ")
f=open("file.txt","r")
var=f.read()
var=var.split(" ")
for i in var:
    if i == n in var:
         count=count+1

print(n,"=",count)
        
