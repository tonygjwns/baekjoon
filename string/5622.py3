let=input()
temp=0
for i in range(len(let)):
    if ord(let[i]) <= ord('O'):
        temp+=((ord(let[i])-56)//3)
    elif let[i] in "PQRS":
        temp+=8
    elif let[i] in "TUV":
        temp+=9
    else:
        temp+=10
print(temp)