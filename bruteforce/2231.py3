a=int(input())
for i in range(int(a/2),a):
    temp=i
    ttemp=i
    while(ttemp/10>0):
        temp+=ttemp%10
        ttemp=int(ttemp/10)
    if(temp == a):
        print(i)
        break
    if(i==a-1):
        print(0)
        break