import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    x,y=map(int,sys.stdin.readline().split(" "))
    b.append([y,x])

b.sort(key=lambda x: (x[0], x[1]))
for i in range(a):
    print(str(b[i][1])+" "+str(b[i][0]))