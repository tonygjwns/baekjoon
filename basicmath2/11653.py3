import math
a=int(input())
i=2
while (a>1):
    if a%i==0:
        print(i)
        a=a/i
    elif(i>math.sqrt(a)):
        print(int(a))
        a=1
    else:
        i+=1