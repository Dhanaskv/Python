#!/usr/bin/python
arr=["python","script"]
file1=open("f1.txt","w")
for i in range(0,len(arr)):
    print(arr[i])
    file1.write(arr[i])
file1.close()
