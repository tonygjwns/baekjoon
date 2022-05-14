num=int(input())
stars=[[' ' for i in range(num)] for j in range(num)]

def star(size,x,y):
    if(size==1):
        stars[x][y]='*'
    else:
        nextsize=size//3
        for i in range(3):
            for j in range(3):
                if (i!=1 or j!=1):
                    star(nextsize,x+i*nextsize,y+j*nextsize)
star(num,0,0)
for k in stars:
    print(''.join(k))