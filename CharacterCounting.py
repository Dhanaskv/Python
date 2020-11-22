#!/usr/bin/python
file1=open("file.txt","r")
dic={}
var=file1.read()
for i in var:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)
