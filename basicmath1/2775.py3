times=int(input())
for i in range(times):
    floor=int(input())
    room=int(input())
    all_num=[[0 for col in range(room)] for row in range(floor+1)]
    all_num[0]=list(range(1,room+1))
    for j in range(1,floor+1):
        for k in range(room):
            for l in range(0,k+1):
                all_num[j][k]+=all_num[j-1][l]
    print(all_num[floor][room-1])
    