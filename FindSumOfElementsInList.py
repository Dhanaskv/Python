#1/usr/bin/python
L1=[10,20,30,40,50,60]
print("The sum of value is: ",sum(L1))
print("Using another method")
total=0
for i in L1:
    total=total+i
print("The total value is : ",total)
print("using another method")
var=0
i=len(L1)-1
while(i>=0):
    var=var+L1[i]
    i=i-1
print(var)

