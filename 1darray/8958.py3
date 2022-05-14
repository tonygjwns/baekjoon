a=int(input())
for i in range(a):
    stt=input()
    cnt=[0]*len(stt)
    if stt[0]=="O":
        cnt[0]=1
    for j in range(1,len(stt)):
        if stt[j]=="O":
            cnt[j]+=cnt[j-1]+1
    print(sum(cnt))