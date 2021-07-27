# Sudoku_Solver

This is a simple Sudoku Solving game where the Sudoku is randomly generated using Dokuson Module depending upon the difficulty level chosen by the user . The core code is based upon Backtracking algorithm while it is modified for GUI using Pygame 


In a sudoku board, there is a 9x9 grid which are split into 9, 3x3 squares. Your objective is to fill in the grid so that every row, column and individual grid has the numbers 1–9 going through it. This means each column, row and 3x3 grid aren’t allowed to have repeated numbers in them.
The unsolved sudoku grid is input in the source code where each 0 represents a blank space that needs to be filled up with a correct number.
The technique used for solving this question is backtracking which is basically testing each and every possible solution in a particualr step recursively and returning the correct ones.At any point if no possible option is valid or no further action can be taken, it backtracks to the last valid state.

search_blank() function iterates through the grid to check if there is any blank space present (represented by "0" in the grid). If found it returns that position as row and coloumn index  in the grid.

check_valid() function checks if the entered number holds true for that particular position the the grid. It checks if the entered number is unique not only in the assosiated row and coloumn but is also true for the 3x3 grid.
3x3 grids indexes will start at a multiple of 3 so the index of the first grid on the top left will be 0,0 and then the first position in the middle square of the top row would be 0,3 etc. This means if we want to iterate through each square, we want to find the 3x3 square which holds this value and we can very easily do this by using the div function which is written as // which returns the division without remainders. We then need to multiply this by 3 to get the starting index of the square. 
 
solve_grid() function recursively iterates through the grid and for each blank space encountered, it performs a backtracking algorithm.At the point where we run the search_blank() function, and either true or false is obtained. If true, we run the subsequent conditionals. In the if statement, we use the indexes we have gotten from the search_blank() function and assign the value of we have tested to work in that position. This now modifies and updates the grid closing a step towards its completion.Then  the recursion portion of the code is done which is the solve_grid() which will use this updated grid to now run the solve_grid() function again. Thus this means that each time the function is run, we are adding values onto the board array,using which  the program is attempting to solve the solution. This is a form of brute force to solve the method. This recursion will continuously run unless we solve_grid() becomes false or  when the search_blank() function can’t find any blank spaces,hence returning True.
