num=int(input())
people=[]
for i in range(num):
    people.append(list(map(int,input().split(" ")))+[1])
for i in range(len(people)):
    for j in range(len(people)):
        if ((people[i][0]<people[j][0])and (people[i][1]<people[j][1])):
            people[i][2]+=1
ranks=[]
for i in range(num):
    ranks.append(str(people[i][2]))
print(" ".join(ranks))