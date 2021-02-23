from math import infinity 
import random 
import time 




AI = +1 
HUMAN = -1

grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]






def wins(state, player):
    win_states = [
        # rows
        [grid[0][0],grid[0][1],grid[0][2]],
        [grid[1][0],grid[1][1],grid[1][2]],
        [grid[2][0],grid[2][1],grid[2][2]],

        # cols
        [grid[0][0],grid[1][0],grid[2][0]],
        [grid[0][1],grid[1][1],grid[2][1]],
        [grid[0][2],grid[1][2],grid[2][2]],
        
        # diagnoals 
        [grid[0][0],grid[1][1],grid[2][2]],
        [grid[2][0],grid[1][1],grid[0][2]],
    ]
    if [player, player, player] in win_states: return True
    else: return False


def evaluate(state):
    if wins(state, AI):
        score = +1
    elif wins(state, HUMAN):
        score = -1 
    else: 
        score = 0
    return score


def gameOver(state):
    return wins(state, HUMAN) or wins(state. AI)


def emptyCell(state):
    cells = []

    for x, row in enumerate(state):
        for y , cell in enumerate(row):
            if cell == 0 : 
                cells.append([x, y])
    return cells

def validMove(x, y):
    if [x, y] in emptyCell(board): return True
    else: return False


def setMove(x, y, player):
    if validMove(x, y):
        board[x][y] = player
        return True 
    else: return False


def minimax(state, depth, player):
    if player == AI:
        best = [-1, -1, -infinity]
    else: 
        best = [-1, -1, +infinity]


    if depth == 0 or gameOver(state):
        score = evaluate(state)
        return [-1, -1, score]
    for cell in emptyCell(state):
        x, y = cell
        state[x][y] = player
          = minimax(state, depth - 1, -player)
        state[x][y] = 0 
        score[0], score[1] = x, y 


        if player == AI: 
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score 

    return best 