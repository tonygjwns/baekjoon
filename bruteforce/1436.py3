a=int(input())
num=666
count=1
while(count!=a):
    num+=1
    while("666" not in str(num)):
        num+=1
    count+=1
print(num)