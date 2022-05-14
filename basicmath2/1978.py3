n=int(input())
numlist=list(map(int,input().split(" ")))
primelist=[2,3]
for i in range(4,1000):
    for j in range(len(primelist)):
        if i%primelist[j]==0:
            break
        if j==(len(primelist)-1):
            primelist.append(i)
count=0
for num in numlist:
    if num in primelist:
        count+=1
print(count)