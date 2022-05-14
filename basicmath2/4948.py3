import math
inlist=[]
a=int(input())
while (a!=0):
    inlist.append(a)
    a=int(input())
def isprime(a):
    if (a==1):
        return False
    elif (a==2):
        return True
    for i in range(2,int(math.sqrt(a)+1)):
        if (a%i==0):
            return False
    return True
primelist=[2]
for i in range(3,max(inlist)*2):
    if (isprime(i)):
        primelist.append(i)
def findab(x):
    if(x==1):
        return 0,0
    a=0
    b=0
    while primelist[a]<=x:
        a+=1
    b=a
    while primelist[b]<=2*x:
        b+=1
        if b==(len(primelist)):
            break

    return a,b-1
        
for i in range(len(inlist)):
    x,y=findab(inlist[i])   
    print(y-x+1)