a,b = map(int,input().split())
board=[]
for i in range(a):
    board.append(input())
check="W"
min_count=64
for i in range(a-7):
    for j in range(b-7):
        count=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if(check!=board[k][l]):
                    count+=1
                if((check=="W")and(l!=j+7)):
                    check="B"
                elif((check=="B")and(l!=j+7)):
                    check="W"
                else:
                    continue
        if((count<min_count)or ((64-count)<min_count)):
            min_count=min(count,64-count)
print(min_count)