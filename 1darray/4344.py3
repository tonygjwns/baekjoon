a=int(input())
for i in range(a):
    lst=list(map(int,input().split()))
    num=lst[0]
    avg=sum(lst[1:])/num
    temp=0
    for j in range(1,num+1):
        if lst[j]>avg:
            temp+=1
    rate=temp/num*100
    print(f"{rate:.3f}%")