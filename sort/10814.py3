num=int(input())
b=[]
for i in range(num):
    x,y=input().split(" ")
    b.append([int(x),i,y])
b.sort(key=lambda x:(x[0],x[1]))
for i in b:
    print(str(i[0])+" "+i[2])