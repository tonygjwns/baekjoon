a,b=map(int,input().split())
lst=list(map(int,input().split()))
cnt=0
for i in range(a):
    if lst[i]<b:
        print(lst[i], end=" ")