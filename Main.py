# Sudoku solver
import numpy as np
import time
start_time = time.time()

hello

grid = [[0,2,0,0,5,0,0,0,7],
        [3,0,4,0,0,1,9,0,6],
        [0,9,0,0,4,0,8,1,5],
        [5,0,0,0,6,0,4,0,3],
        [4,0,0,2,0,0,1,0,9],
        [0,0,9,0,0,0,0,6,0],
        [0,8,0,0,1,0,2,7,0],
        [7,6,0,0,0,0,0,0,0],
        [0,0,0,8,0,0,0,0,0]]

grid1 = [[0,0,2,0,0,0,0,7,0],
        [1,8,0,7,0,3,0,2,0],
        [3,0,4,0,0,0,0,0,1],
        [5,3,1,0,0,0,9,0,4],
        [8,0,0,0,4,9,6,0,0],
        [0,4,0,8,0,0,0,5,7],
        [0,9,6,0,5,7,8,3,0],
        [0,1,0,3,9,6,0,4,0],
        [0,5,0,2,8,0,0,9,0]]

numberOfSolutions = 0

def possible(y,x,testnumber):
    for i in range(0,9):
        if grid[y][i] == testnumber:
            return False
    for i in range(0, 9):
        if grid[i][x] == testnumber:
            return False
    yField = (y//3)*3
    xField = (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[yField+i][xField+j] == testnumber:
                return False
    return True

def solve():
    global grid
    global a
    global numberOfSolutions
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for testnumber in range(1,10):
                    if possible(y,x,testnumber):
                        grid[y][x] = testnumber
                        solve()

                        a = np.array(grid)
                        if np.all(a!=0):
                            print("found solution")
                            print(np.matrix(grid))
                            numberOfSolutions = numberOfSolutions + 1

                        grid[y][x] = 0
                return

def solveNotWorking():
    global grid
    noteGrid = np.zeros((9, 9, 1))

    # put grid in noteGrid if valueOfGrid is not 0. Else put all the possible numbers
    for y in range(9):
        for x in range(9):
            valueInGrid = grid[y][x]
            if valueInGrid != 0:
                noteGrid[y,x,valueInGrid] = valueInGrid
            else:
                for i in range(1,10):
                    count = 0
                    if possible(y,x,i):
                        count += 1
                        noteGrid[y,x,i] = i
                if count == 1: grid[y][x] = noteGrid[y,x,]


    #print(noteGrid)





solve()
print("number of solutions:", numberOfSolutions)



#print(np.matrix(grid))
#input("More?")



print("time elapsed: {:.4f}s".format(time.time() - start_time))

# -------------------------------


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#

import numpy as np

## =========       ===================
grid = [[7, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 5, 0, 0, 0, 0, 0, 4, 3],
        [3, 7, 6, 1, 4, 2, 5, 9, 8],
        [0, 0, 1, 0, 9, 0, 2, 0, 0],
        [5, 0, 0, 7, 6, 8, 3, 1, 4]]


grid1 = [[0, 2, 0, 0, 5, 0, 0, 0, 7],
        [3, 0, 4, 0, 0, 1, 9, 0, 6],
        [0, 9, 0, 0, 4, 0, 8, 1, 5],
        [5, 0, 0, 0, 6, 0, 4, 0, 3],
        [4, 0, 0, 2, 0, 0, 1, 0, 9],
        [0, 0, 9, 0, 0, 0, 0, 6, 0],
        [0, 8, 0, 0, 1, 0, 2, 7, 0],
        [7, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0]]

grid2 = [[9, 0, 6, 0, 7, 0, 4, 0, 3],
         [0, 0, 0, 4, 0, 0, 2, 0, 0],
         [0, 7, 0, 0, 2, 3, 0, 1, 0],
         [5, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 4, 0, 2, 0, 8, 0, 6, 0],
         [0, 0, 3, 0, 0, 0, 0, 0, 5],
         [0, 3, 0, 7, 0, 0, 0, 5, 0],
         [0, 0, 7, 0, 0, 5, 0, 0, 0],
         [4, 0, 5, 0, 1, 0, 7, 0, 8]]


# numberOfSolutions = 0
## -----------------------------------

## ============================
#
#
def possible(grid, y, x, number):
    for i in range(0, 9):
        # global grid
        if grid[y][i] == number:
            return False
        for i in range(0, 9):
            if grid[i][x] == number:
                return False
        yField = (y // 3) * 3
        xField = (x // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if grid[yField + i][xField + j] == number:
                    return False
    return True


## ============================
#
#
def showGrid(grid):
    print("found solution")
    print(np.matrix(grid))


## ============================
#
#
def solve(grid, numberOfSolutions):
    # global grid
    # global a
    # global numberOfSolutions
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for testnumber in range(1, 10):
                    if possible(grid, y, x, testnumber):
                        grid[y][x] = testnumber
                        numberOfSolutions = solve(grid, numberOfSolutions)

                        a = np.array(grid)
                        if np.all(a != 0):
                            showGrid(grid)
                            numberOfSolutions = numberOfSolutions + 1

                        grid[y][x] = 0

                return numberOfSolutions
    return numberOfSolutions


## ============================
#
#
def hello():
    print("   ____       _ _ _                            _      ")
    print("  / ___|_   _(_) | | __ _ _   _ _ __ ___   ___( )___  ")
    print(" | |  _| | | | | | |/ _` | | | | '_ ` _ \ / _ \// __| ")
    print(" | |_| | |_| | | | | (_| | |_| | | | | | |  __/ \__ \ ")
    print("  \____|\__,_|_|_|_|\__,_|\__,_|_| |_| |_|\___| |___/ ")

    print("  ____            _       _           ")
    print(" / ___| _   _  __| | ___ | | ___   _  ")
    print(" \___ \| | | |/ _` |/ _ \| |/ / | | | ")
    print("  ___) | |_| | (_| | (_) |   <| |_| | ")
    print(" |____/ \__,_|\__,_|\___/|_|\_\\__,__| ")

    print("")


## ============================
#
#
def main(args):
    # print('hello \n')
    hello()

    print("=== Grid ===")
    numberOfSolutions = 0
    numberOfSolutions = solve(grid, numberOfSolutions)
    print('number of solutions:', numberOfSolutions)
    print("------------\n")

    print("=== Grid2 ===")
    numberOfSolutions = 0
    numberOfSolutions = solve(grid2, numberOfSolutions)
    print('number of solutions:', numberOfSolutions)
    print("------------\n")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
