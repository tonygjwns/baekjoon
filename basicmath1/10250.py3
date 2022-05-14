num=int(input())
for i in range(num):
    a,b,c=map(int,input().split())
    if c%a==0:
        floor = a
    else:
        floor = c%a
    room=(c-1)//a+1
    print(floor*100+room)