#!/usr/bin/program
var="malayalam"
i=0
j=len(var)-1
while(i<=j):
    if var[i] == var[j]:
        i=i+1
        j=j-1
    else:
        print("it is not palindrome")
        break
if j<i:
    print("This is palindrome")
