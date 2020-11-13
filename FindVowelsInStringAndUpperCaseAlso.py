#!/usr/bin/python
str1="pythonprogramminglanguage"
var1=0
var2=0
var3=0
var4=0
var5=0
if ("a" in str1) or ("A" in str1):
    var1=1
if ("e" in str1) or ("E" in str1):
    var2=1
if ("i" in str1) or ("I" in str1):
    var3=1
if ("o" in str1) or ("O" in str1):
    var4=1
if ("u" in str1) or ("U" in str1):
    var5=1



if (var1==1) and (var2==1) and (var3==1) and (var4==1) and (var5==1):
    print("vowels is there")
else:
    print("no vowels")
