inp=int(input())
def isprime(a):
    if (a==1):
        return False
    elif (a==2):
        return True
    for i in range(2,a):
        if (a%i==0):
            return False
    return True
inlist=[]
for i in range(inp):
    j=int(input())
    inlist.append(j)
primelist=[2]

def findab(x,lst):
    a=x//2
    b=x-a
    while(True):
        if((a in lst) and (b in lst)):
            return a,b
        a+=1
        b=x-a
for i in range(3,10001):
    if (isprime(i)):
        primelist.append(i)
for k in range(inp):
    x,y=findab(inlist[k],primelist)
    print(str(y)+" "+str(x))