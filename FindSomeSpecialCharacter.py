#!/usr/bin/python
str1="geeksforgeeks@aaa"
count=0
for i in str1:
    if (ord(i) >= 65) and (ord(i) <= 90) or (ord(i) >= 97) and (ord(i) <= 122):
        pass
    else:
        count=1
        break
if count:
    print("special character is there")
else:
    print("no special character")
