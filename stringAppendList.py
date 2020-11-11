#!/usr/bin/python
str1="python scripting language"
L1=[]
str1=str1.split(" ")
for i in range(len(str1)-1,-1,-1):
    L1.append(L1[i])
print(L1)

