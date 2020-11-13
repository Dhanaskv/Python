#!/usr/bin/python
str1="pythoninterpreterlanguage"
allfreq={}
for i in str1:
    if i in allfreq:
        allfreq[i]=allfreq[i]+1
    else:
        allfreq[i]=1
for var in allfreq:
    print("key="+var)
    print("value="+str(allfreq[var]))
maxkey=""
maxvalue=0
for i in allfreq:
    if (allfreq[i]>maxvalue):
        maxvalue=allfreq[i]
        maxkey=i
print(maxkey,maxvalue)
