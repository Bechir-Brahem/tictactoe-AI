"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    n=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!=EMPTY:
                n+=1
    if(n%2==0):
        return X
    return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves=set()
    for i in range(3):
        for j in range(3):
            if(board[i][j]==EMPTY):
                moves.add((i,j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tmp_board=[]
    for i in board:
        tmp_board.append(list(i))
    if(tmp_board[action[0]][action[1]]!=EMPTY):
        raise Exception("wrong action in result()")
    tmp_board[action[0]][action[1]]=player(board)
    if(tmp_board==None):
        raise Exception("none in result()")
    return tmp_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if(board==None):
        raise Exception("NONE IN WINNER()")
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            return board[i][0]
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]:
            return board[0][i]
    if all(board[i][i]==board[0][0] for i in range(3)):
        return board[0][0]
    if all(board[i][2-i]==board[1][1] for i in range(3)):
        return board[1][1]
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)!=None):
        return True
    if(actions(board)==set()):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(board==None):
        raise Exception("NONE IN  UTILITY ")
    win=winner(board)
    if win==X:
        return 1
    if win==O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    turn=player(board)
    if(turn ==X):
        best_move=valX(board)
    else:
        best_move=valY(board)
        
    return best_move[1]


def valX(board):
    if(terminal(board)):
        return (utility(board),0)
    v=-2
    l=actions(board)
    move=next(iter(l))
    for action in l:
        tmp=valY(result(board,action))
        if(tmp[0]>=v):
            move=action
            v=tmp[0]
        if(tmp[0]==1):
            break
    return (v,move)

def valY(board):
    if(terminal(board)):
        return (utility(board),0)
    v=2
    l=actions(board)
    move=next(iter(l))
    for action in l:
        tmp=valX(result(board,action))
        if(tmp[0]<=v):
            move=action
            v=tmp[0]
        if(tmp[0]==-1): break
    return (v,move)
