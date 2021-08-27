# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 19:14:14 2021

@author: tyler
"""

#initilizing variables
grid = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]

every_option = [] #contains a list from 1 to 9 for every position on the board
for i in range(9): 
    every_row = []
    every_option.append(every_row)
    print('')
    for j in range(9):
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   
        every_row.append(options)
        print(grid[i][j], end='')

box_layout = [] #3 by 3 of possible solutions
for i in range(3): #produces box templet of 3 by 3 of possible options
    box_row = []
    box_layout.append(box_row)
    for i in range(3):
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   
        box_row.append(options)

def my_board(row, col, num): #adds to specific grid locations
    grid[row-1][col-1] = num
    
def update_box(row, col): # takes out numbers inside unsolved slots within its specified box
    if grid[row][col] in box_layout[int(row/3)][int(col/3)]:
        box_layout[int(row/3)][int(col/3)].remove(grid[row][col])
        for i in range(9):
            for j in range(9):
                if box_layout[int(row/3)][int(col/3)] is box_layout[int(i/3)][int(j/3)] and grid[i][j] == "0" and grid[row][col] in every_option[i][j]:
                    every_option[i][j].remove(grid[row][col])

def check(): #Determins whether the game is over or not
    game_over = True
    for i in grid:
        for j in i:
            if j == '0':
                game_over = False
    return game_over

def line_check(row, col):
    for x in range(9):
        if every_option[row][col][x] not in grid[row]:
            tic = 0
            #seeing how many are inside the row and seeing if its only in one box
            for i in range(9):
                if every_option[row][col][x] not in every_option[row][x]:
                    tic += 1
                    if tic >= 8: 
                        pass
            


user_input =  input("What would you like to do; 'add', 'print', 'stop', or 'solve'?\n-")

while user_input.lower() != "stop":
    
    if user_input.lower() == "add": #will ask for the parameters to add a slot to the grid
        try: #used if input is not a number or wants to stop
            continue_adding = True
            while continue_adding is True:
                row = int(input("type non number phrase to stop otherwise... \nwhich horozontal line is the number in (1 being top most, 9 being bottom most): "))
                col = int(input("type non number phrase to stop otherwise... \nwhich vertial line is the number on (1 being left most, 9 being right most): "))
                num = int(input("type non number phrase to stop otherwise... \nwhat number is: "))
                
                if row >= 1 and row <= 9 and col >= 1 and col <= 9 and num >= 0 and num <= 9:
                    my_board(row, col, str(num)) #adding to grid
                print("added!!!")
        except:
            print("------------------------\n Stopping adding process \n------------------------")
            
    elif user_input.lower() == "print": #displays the grid
        for i in range(9):
            print('')
            if (i-1) % 3 == 2:
                print('')
            for j in range(9):
                print(grid[i][j], end='')
                if j % 3 == 2:
                    print(" ", end='')
        
    elif user_input.lower() == "solve": #solves the sudoku board
        
        while check() is False:
            for i in range(9): #subtracting already used number in row, col, box
                for j in range(9):
                    if grid[i][j] != "0": #if it is a number then checks that same number cant be in row, col, or box
                        every_option[i][j] = grid[i][j]
                        update_box(i, j)
                        for x in range(9): # takes out # from the vert and horozontal rows
                            if grid[i][j] in every_option[x][j] and every_option[x][j] != grid[i][j]:
                                every_option[x][j].remove(grid[i][j])
                            else:
                                if len(every_option[x][j]) == 1:
                                    grid[x][j] = every_option[x][j][0]
                                else:
                                    pass
                            if grid[i][j] in every_option[i][x] and every_option[i][x] != grid[i][j]:
                                every_option[i][x].remove(grid[i][j])
                            else:
                                if len(every_option[i][x]) == 1:
                                    grid[i][x] = every_option[i][x][0]
                                else:
                                        pass
                    elif grid[i][j] == "0":
                        # print("row, col:", i,j)
                        for slot in range(len(every_option[i][j])):
                            clear_h = 0
                            clear_v = 0
                            if grid[i][j] == "0": #checks to see if still 0
                                for x in range(9):
                                    if every_option[i][j][slot] not in every_option[x][j]:
                                        clear_h += 1
                                        if clear_h == 8:
                                            grid[i][j] = every_option[i][j][slot]
                                        else:
                                            pass
                                    if every_option[i][j][slot] not in every_option[i][x]:
                                        clear_v += 1
                                        if clear_v == 8:
                                            grid[i][j] = every_option[i][j][slot]
                        
                    else:
                        print("Something went wrong")
                        
        print("\n Sudoku is Complete")
        
    
    else:
        print("------------------------\n Error: Unknown command\n------------------------")
    #asks for a new input
    user_input = input("What would you like to do; 'add', 'print', 'stop', or 'solve'?\n-")
    continue














