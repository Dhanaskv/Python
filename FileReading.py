#!/usr/bin/python
file1=open("file.txt","r")
var=file1.read()
dic={}
var=var.split(" ")
for i in var:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)


