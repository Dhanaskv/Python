#!/bin/python
dic={}
file1=open("File1.txt","r")
var=file1.read()
var=var.split(" ")
for i in var:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)


