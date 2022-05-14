def find(n):
    if n<100:
        return 1
    else:
        if (n//100-(n//10)%10) == ((n//10)%10-n%10):
            return 1
        else:
            return 0
num=int(input())
if num<100:
    print(num)
else:
    cnt=99
    for i in range(100,num+1):
        cnt+=find(i)
    print(cnt)