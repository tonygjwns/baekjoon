def d(n):
    n=n+sum(map(int,str(n)))
    return n
def selfnum(n,lst):
    n=d(n)
    if n<10000:
        lst.append(n)
    return
numlist=list(range(1,10000))
notlist=[]
for i in range(len(numlist)):
    selfnum(numlist[i],notlist)
relist=list(set(notlist))
for i in range(len(relist)):
    numlist.remove(relist[i])
for i in range(len(numlist)):
    print(numlist[i])