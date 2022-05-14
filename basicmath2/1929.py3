import math
a,b=map(int,input().split())
def isprime(a):
    if (a==1):
        return False
    elif (a==2):
        return True
    for i in range(2,int(math.sqrt(a)+1)):
        if (a%i==0):
            return False
    return True
for num in range(a,b+1):
    if (isprime(num)):
        print(num)