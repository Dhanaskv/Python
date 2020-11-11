#!/usr/bin/python
str1="python scripting world"
L1=[]
str1=str1.split(" ")
n=len(str1)-1
for i in str1:
    L1.append(i)
print(L1)
str1=""
for i in range(len(L1)-1,-1,-1):
    str1=str1+L1[i]+" "
print(str1)
