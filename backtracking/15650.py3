n,m=map(int,input().split())
s=[]
count=0
def f(count):
    if (len(s)==m):
        print(" ".join(map(str,s)))
        return
    for i in range(count+1,n+1):
        count=i
        s.append(i)
        f(count)
        s.pop()
f(count)