#!/usr/bin/python
str1="python scripting world and simple interpreter"
n=input("The user input value is: ")
str1=str1.split(" ")
for i in str1:
    if len(i) == int(n):
        print(i)
