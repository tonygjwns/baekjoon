xlst=[]
ylst=[]
for i in range(3):
    a,b=map(int,input().split())
    xlst.append(a)
    ylst.append(b)
def finddot(lst):
    temp=sum(lst)-max(lst)-min(lst)
    if(temp != max(lst)):
        return max(lst)
    else:
        return min(lst)
print(str(finddot(xlst))+" "+str(finddot(ylst)))