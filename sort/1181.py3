num=int(input())
b=[]
for _ in range(num):
    b.append(input())
b=list(set(b))
b.sort()
b.sort(key=len)
for i in range(len(b)):
    print(b[i])