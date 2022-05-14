num=int(input())
b=list(map(int,input().split(" ")))
c=list(set(b.copy()))
c.sort()
d=dict()
for i in range(len(c)):
    d[c[i]]=i
    
for i in b:
    print(d[i],end=" ")