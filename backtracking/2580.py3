board=[list(map(int,input().split(" "))) for _ in range(9)]

checker=False

#returns true if number is in
def checkrow(board,row_num ,num):
    return (num in board[row_num])

def checkcol(board, col_num,num):
    for i in range(9):
        if(board[i][col_num]==num):
            return True
    return False
def checkbox(board, row_num,col_num,num):
    temp_row=(row_num//3)*3
    temp_col=(col_num//3)*3
    for i in range(temp_row, temp_row+3):
        for j in range(temp_col,temp_col+3):
            if(board[i][j]==num):
                return True
    return False

def printboard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j],end=" ")
        print("")

def sdk(i,j):
    global checker
    
    for i in range(i,9):
        for j in range((j%8),9):
            if(board[i][j]==0):
                for k in range(1,10):
                    if(checkrow(board, i,k) or checkcol(board,j,k) or checkbox(board,i,j,k)):
                        if(k==9):
                            board[i][j]=0
                            return
                        continue
                    board[i][j]=k
                    sdk(i,j)
                    if (checker):
                        return
                    board[i][j]=0
                    if(k==9):
                        return

            if((i==8) and (j==8)):
                checker=True
                return
sdk(0,0)
printboard(board)