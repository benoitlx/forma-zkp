# Python program to generate a valid sudoku 
# with k empty cells

import random
import copy

# Returns false if given 3x3 block contains num
# Ensure the number is not used in the box
def unUsedInBox(grid, rowStart, colStart, num):
    for i in range(3):
        for j in range(3):
            if grid[rowStart + i][colStart + j] == num:
                return False
    return True

# Fill a 3x3 matrix
# Assign valid random numbers to the 3x3 subgrid
def fillBox(grid, row, col):
    for i in range(3):
        for j in range(3):
            while True:
                
                # Generate a random number between 1 and 9
                num = random.randint(1, 9)
                if unUsedInBox(grid, row, col, num):
                    break
            grid[row + i][col + j] = num

# Check if it's safe to put num in row i
# Ensure num is not already used in the row
def unUsedInRow(grid, i, num):
    return num not in grid[i]

# Check if it's safe to put num in column j
# Ensure num is not already used in the column
def unUsedInCol(grid, j, num):
    for i in range(9):
        if grid[i][j] == num:
            return False
    return True

# Check if it's safe to put num in the cell (i, j)
# Ensure num is not used in row, column, or box
def checkIfSafe(grid, i, j, num):
    return (unUsedInRow(grid, i, num) and 
            unUsedInCol(grid, j, num) and 
            unUsedInBox(grid, i - i % 3, j - j % 3, num))

# Fill the diagonal 3x3 matrices
# The diagonal blocks are filled to simplify the process
def fillDiagonal(grid):
    for i in range(0, 9, 3):
        
        # Fill each 3x3 subgrid diagonally
        fillBox(grid, i, i)

# Fill remaining blocks in the grid
# Recursively fill the remaining cells with valid numbers
def fillRemaining(grid, i, j):
    
    # If we've reached the end of the grid
    if i == 9:
        return True
    
    # Move to next row when current row is finished
    if j == 9:
        return fillRemaining(grid, i + 1, 0)
    
    # Skip if cell is already filled
    if grid[i][j] != 0:
        return fillRemaining(grid, i, j + 1)
    
    # Try numbers 1-9 in current cell
    for num in range(1, 10):
        if checkIfSafe(grid, i, j, num):
            grid[i][j] = num
            if fillRemaining(grid, i, j + 1):
                return True
            grid[i][j] = 0 
    
    return False

# Remove K digits randomly from the grid
# This will create a Sudoku puzzle by removing digits
def removeKDigits(grid, k):
    while k > 0:
        
        # Pick a random cell
        cellId = random.randint(0, 80)

        # Get the row index
        i = cellId // 9

        # Get the column index
        j = cellId % 9

        # Remove the digit if the cell is not already empty
        if grid[i][j] != 0:
            # Empty the cell
            grid[i][j] = 0
            # Decrease the count of digits to remove
            k -= 1

# Generate a Sudoku grid with K empty cells
def sudokuGenerator(k):
    
    # Initialize an empty 9x9 grid
    grid = [[0] * 9 for _ in range(9)]

    # Fill the diagonal 3x3 matrices
    fillDiagonal(grid)

    # Fill the remaining blocks in the grid
    fillRemaining(grid, 0, 0)

    # Remove K digits randomly to create the puzzle
    removeKDigits(grid, k)

    return grid

board = [[0] * 9 for _ in range(9)]
fillDiagonal(board)
fillRemaining(board, 0, 0)
solution = copy.deepcopy(board)
removeKDigits(board, 20)

def print_board(board):
    base = 3
    side = base*base
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
    line0  = expandLine("╔═══╤═══╦═══╗")
    line1  = expandLine("║ . │ . ║ . ║")
    line2  = expandLine("╟───┼───╫───╢")
    line3  = expandLine("╠═══╪═══╬═══╣")
    line4  = expandLine("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums   = [ [""]+[symbol[n] for n in row] for row in board ]
    print(line0)
    for r in range(1,side+1):
        print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
        print([line2,line3,line4][(r%side==0)+(r%base==0)])

