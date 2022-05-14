import sys
num=sys.stdin.readline()
a=int(num)
b=[0]*10001
for i in range(a):
    temp= int(sys.stdin.readline())
    b[temp]+=1
for i in range(len(b)):
    if(b[i]!=0):
        for j in range(b[i]):
            print(i)