a=int(input())
lst=list(map(int,input().split()))
num=max(lst)
tot=0
for i in range(a):
    tot+=lst[i]/num*100
print(tot/a)