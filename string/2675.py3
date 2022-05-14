num = int(input())
for i in range(num):
        a,b = input().split(" ")
        a= int(a)
        temp=""
        for j in b:
            temp= temp+j*a
        print(temp)