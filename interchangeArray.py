#!/usr/bin/python
array=[10,20,30,40,50,60]
for i in range(0,len(array)-1,2):
    sum1=array[i]
    array[i]=array[i+1]
    array[i+1]=sum1
print("The interchange value:",array)
