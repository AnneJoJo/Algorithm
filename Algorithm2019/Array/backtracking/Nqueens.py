
def Nqueens(N):

    def check(board,x,y):
            #print(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][y] == "Q": return False
                if board[r][c] == "Q" and abs(r-c) == abs(x-y):
                    return False
        return True



    def place(N,board,x,res):
        if x == N:
            res.append(board)
            return
        row = ['.']* N
        for i in range(N):
            if check(board,x,i):
                place(N,board+[row[:i]+['Q']+row[i+1:]],x+1,res) #

    res = []
    place(N,[],0,res)
    print(res)



Nqueens(4)


