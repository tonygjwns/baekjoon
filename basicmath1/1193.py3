num=int(input())
row=1
tot=1
need=0
while num>tot:
    row+=1
    tot+=row
    need=tot-num
    
if row%2 ==1:
    a=1+need
    b=row-need
    print(str(a)+"/"+str(b))
else:
    a=row-need
    b=1+need
    print(str(a)+"/"+str(b))
