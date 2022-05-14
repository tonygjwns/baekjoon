n=int(input())
board=[0 for r1 in range(n)]
count=[0]

def Q(row):
    if(row==n):
        count[0]+=1
        return
    for i in range(n):
        checker=True
        for j in range(row):
            #현재 row 까지 뒤져 봤을 때 놔도 되는가.
            if(board[j]==(i+1) or (((board[j])-i-1)==(j-row))) or ((board[j]-i-1)==(row-j)):
                checker=False
                break
        if(checker):
            board[row]=(i+1)
            row+=1
            Q(row)
            row-=1
    board[row-1]=0
    return
            
        #[0]에 1

Q(0)
print(count[0])