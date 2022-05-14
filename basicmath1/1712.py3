import math
a,b,c=map(int,input().split())
if b>=c:
    if a==0:
        print(1)
    else:
        print(-1)
else:
    print(math.ceil((a+1)/(c-b)))