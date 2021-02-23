from math import infinity 
import random 
import time 



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



    