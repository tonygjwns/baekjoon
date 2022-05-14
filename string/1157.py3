target = input().lower()
lst=[0]*26
import string
for i in range(len(target)):
    
    lst[ord(target[i])-97]+=1
num=max(lst)
if lst.count(num)>1:
    print("?")
else:
    print(chr(lst.index(num)+97).upper())