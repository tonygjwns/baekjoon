import string
a=input()
for i in range(len(string.ascii_lowercase)):
    if string.ascii_lowercase[i] in a:
        print(a.index(string.ascii_lowercase[i]),end=" ")
    else:
        print(-1, end=" ")