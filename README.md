# Sudoku
The outcome of this project is to give you, the user, a full completed sudoku puzzle after you have inputed numbers.

# How it works
In order for this program to work the user will be prompted with options such as add, print, stop, or solve. Initially the sudoku board is empty so, 
"add' lets you input a number into the sudoku board (NOTE: you must add before you can solve). "print" prints the current board. "stop" stops the program. 
Lastly, "solve" solves the board after numbers have been added.  This program solves the sudoku board logicaly just like how a normal person would try to
solve it. Once solving the puzzle if the puzzle is unsolvable and/or is an expert sudoku board the code will fail to print a solution. 

# Bugs
As of right now I am missing one piece of logic to fully completing this. The logic that is missing is if there are three spots in a 3 by 3 square that are empty
but two of them have two numbers solely to those two spots while a third number has one to all three, that third number goes into the one that isn't occupied by
those two (This is a problem because there can be mulitple numbers on the squares but it wouldn't matter as long as the these conditions are true).


