a,b = map(int, input().split(" "))
c=list(map(int,input().split(" ")))
c=sorted(c)
max_num=0
for i in range(len(c)-2):
    for j in range(i+1,len(c)-1):
        for k in range(j+1,len(c)):
            temp=c[i]+c[j]+c[k]
            if((temp>max_num)and temp<=b):
                max_num=temp
            if(max_num==b):
                break               
print(max_num)