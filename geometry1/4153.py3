a,b,c=map(int,input().split())
while(a!=0 and b!=0 and c!=0):
    if((a**2+b**2+c**2)==2*(max(a,b,c))**2):
        print("right")
    else:
        print("wrong")
    a,b,c=map(int,input().split())