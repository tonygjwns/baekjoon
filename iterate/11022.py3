inp=int(input())
for i in range(inp):
    a,b=map(int,input().split())
    a1=i+1
    a2=a
    a3=b
    a4=a+b
    text = f"Case #{a1}: {a2} + {a3} = {a4}"
    print(text)