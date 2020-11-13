#!/usr/bin/python
dic1={"a":0,"e":0,"i":0,"o":0,"u":0}
str1="pythonworld"
count=0
for i in str1:
    if i in dic1:
        dic1[i]=1
    
for i in dic1:
    if dic1[i] == 0:
        count=1
        break

if count:
    print("it is no vowels")
else:
    print("vowels in there")
    
    

