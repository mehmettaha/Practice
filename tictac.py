import numpy
board = [[0,0,0], [0,0,0],[0,0,0]]

def tictac(board):
    for i in range(3):
        print(3 * " ---")
        print("| %d | %d | %d |" % (board[i][0], board[i][1], board[i][2]))
    print(3 * " ---")

def horiz(board):
    for line in board:
        if line[0] == line[1] == line[2] and line[0] != 0:
            print("Player %d wins!" % line[0])
            return True
        else:
            return False

def vert(board):
    board = numpy.transpose(board)
    for line in board:
        if line[0] == line[1] == line[2] and line[0] != 0:
            print("Player %d wins!" % line[0])
            return True
        else:
            return False        

def diag(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        print("Player %d wins!" % board[0][0])
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        print("Player %d wins!" % board[0][2])
        return True
    else: 
        return False

def game(board):
    if horiz(board) is False:
        if vert(board) is False:
            if diag(board) is False:
                return True
    return False

i = 0
while game(board):
    tictac(board)
    print("Player %d" % (i%2+1))
    tup= tuple(input("Enter your position as 'xy'"))
    x, y = tup
    x, y = int(x)-1, int(y)-1
    if i % 2 == 0:
        board[x][y] = 1
    else:
        board[x][y] = 2
    i += 1
        
