#!/usr/bin/python
def ratio(str1):
    count=0
    for i in str1:
        if int(i) != 0 and int(i) !=1:
            count=1
            break
        else:
            pass
    if count:
        print("It is not binary string")
    else:
        print("It is binary string")
str1="0010101010100110"
ratio(str1)
