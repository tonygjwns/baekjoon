n=int(input())
nums=[]
for _ in range(n):
    nums.append(list(map(int,input().split(" "))))
total=0
for i in range(n):
    for j in range(n):
        total+=nums[i][j]
team=[0 for r1 in range(n//2)]

difference=total

def calculate(teams):
    temp=0
    for i in range(len(teams)):
        for j in range(len(teams)):
            temp+=nums[teams[i]][teams[j]]
    temp1=0
    opponents=[]
    for k in range(n):
        if k not in teams:
            opponents.append(k)
    for i in range(len(teams)):
        for j in range(len(teams)):
            temp1+=nums[opponents[i]][opponents[j]]

    return abs(temp-temp1)
            

def dfs(count,total,n,now):
    global difference
    if count==(n//2):
        temp=calculate(team)
        difference=min(difference,temp)
        return
    for j in range(now+1,n):
        team[count]=j
        dfs(count+1,total,n,j)    
    
dfs(1,total,n,0)
print(difference)