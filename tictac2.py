import numpy
board = [[1,0,1], [1,1,2],[1,2,1]]

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
    elif board[0][2] == board[1][1] == board[2][0] and board[0][0] != 0:
        print("Player %d wins!" % board[0][2])
        return True
    else: 
        return False

def game(board):
    if horiz(board) is False:
        if vert(board) is False:
            if diag(board) is False:
                print("Noone won")
game(board)





