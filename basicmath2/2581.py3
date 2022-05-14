import math
a=int(input())
b=int(input())
def isprime(a):
    if (a==1):
        return False
    elif (a==2):
        return True
    for i in range(2,int(math.sqrt(a)+1)):
        if (a%i==0):
            return False
    return True
lst=[]
for i in range(a,b+1):
    if (isprime(i)):
        lst.append(i)


if(len(lst)==0):
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
