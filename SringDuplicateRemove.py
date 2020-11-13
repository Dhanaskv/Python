#!/usr/bin/python
str1="GeeksForGeeks"
dic={}
for i in str1:
    if i not in dic:
        dic[i]=1
        print(i)

