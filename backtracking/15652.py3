n,m=map(int,input().split(" "))
count=1
t=[]
def f(count):
    if(len(t)==m):
        print(" ".join(map(str,t)))
        return
    for i in range(count,n+1):
        t.append(i)
        f(count)
        t.pop()
        count+=1
f(count)