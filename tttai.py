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
    