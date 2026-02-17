Technical Briefing: Pygame Sudoku Implementation and Backtracking Logic

Executive Summary

This document provides a technical synthesis of a Sudoku application implemented using the Pygame library and a recursive backtracking algorithm. The system integrates real-time user interaction with a robust logical backend to provide a fully functional puzzle game. Key features include dynamic grid generation based on user-defined difficulty levels (Easy, Medium, Hard), a dual-input system for "sketching" and "placing" numbers, and an automated solver that validates moves. The application tracks player performance through a strike system and a real-time clock, while the underlying logic ensures puzzle integrity by verifying moves against row, column, and 3x3 sub-grid constraints.


--------------------------------------------------------------------------------


System Architecture and Configuration

The application is built on a modular structure that separates the graphical user interface (GUI) from the mathematical puzzle logic. It relies on several key libraries:

* Pygame: Manages the window rendering, event handling (keyboard/mouse), and font drawing.
* Dokusan: Utilized for generating random Sudoku puzzles.
* NumPy: Used for array manipulation and reshaping the puzzle grid into a 9x9 matrix.

Difficulty Scaling

Upon initialization, the system prompts the user to select a difficulty level. This selection determines the avg_rank parameter passed to the puzzle generator:

Difficulty Level	Input Identifiers	Rank Value (N)
HARD	'HARD', 'Hard', 'H'	180
MEDIUM	'MEDIUM', 'Medium', 'M'	120
EASY	'EASY', 'Easy', 'E'	60


--------------------------------------------------------------------------------


Core Logic and Solver Mechanics

The integrity of the game is maintained through a recursive backtracking algorithm and a comprehensive validation function.

Validation Constraints (check_valid)

Every move, whether made by the user or the solver, must satisfy three primary Sudoku constraints:

1. Row Check: The number must not already exist within the same horizontal row.
2. Column Check: The number must not already exist within the same vertical column.
3. 3x3 Box Check: The number must be unique within its specific 3x3 sub-grid. The system calculates the box coordinates using integer division: x = pos[1] // 3 and y = pos[0] // 3.

Recursive Backtracking Algorithm (solve_grid)

The solver uses a depth-first search strategy to complete the puzzle:

* Search for Blanks: The search_blank function scans the board for the first cell containing a 0.
* Recursive Trial: If a blank is found, the solver attempts to place numbers 1 through 9.
* Backtracking: If a placement leads to a state where no numbers can satisfy the constraints in subsequent cells, the function resets the current cell (board[row][col] = 0) and backtracks to the previous state.
* Base Case: When no blank squares remain, the puzzle is considered solved, and the function returns True.


--------------------------------------------------------------------------------


User Interface and Interaction Design

The GUI is managed through two primary classes: Sudoku_Grid and Cube.

The Sudoku_Grid Class

This class represents the entire 9x9 board. It manages the collection of Cube objects and handles high-level grid operations:

* Grid Rendering: Draws the board lines, using thicker lines every three cells to distinguish the 3x3 sub-grids.
* Selection: Tracks which cell is currently targeted by the user via mouse click.
* Placement Logic: When a user attempts to place a number (pressing 'Enter'), the grid validates the move against the solver logic. If the move is invalid or makes the puzzle unsolvable, the move is rejected.

The Cube Class

Each individual cell is an instance of the Cube class, which manages its own state:

* Permanent Values (val): Numbers that are part of the original puzzle or correctly placed by the user. These are rendered in black.
* Temporary Values (temp): "Sketched" numbers that the user is considering. These are rendered in gray in the top-left corner of the cell.
* Selection State: Highlighted with a red border when active.


--------------------------------------------------------------------------------


Gameplay Mechanics and Controls

The application features a real-time game loop that monitors for specific user inputs:

Input Mapping

* Keys 1-9: Used to "sketch" a value into the selected cell.
* Delete/Backspace: Clears the temporary value in the selected cell.
* Return (Enter): Confirms the sketched value.
* Mouse Click: Selects a specific cell on the grid.

Performance Tracking

* Strikes: If a user attempts to place an incorrect number (one that does not satisfy the validation and solving logic), a strike is added. Strikes are displayed visually as "X" marks on the interface.
* Timer: A running clock tracks the time elapsed since the game started, formatted in MM:SS.
* Win Condition: The game concludes when all cells are correctly filled. The console outputs "Congratulations! Game over !!" and the application terminates.


--------------------------------------------------------------------------------


Implementation Details

The main() function coordinates the lifecycle of the application:

1. Window Setup: Creates a 540x600 pixel window.
2. Event Processing: Continuously checks for pygame.QUIT, pygame.KEYDOWN, and pygame.MOUSEBUTTONDOWN events.
3. Visual Updates: The redraw_window function refreshes the display, ensuring the timer, strikes, and grid are rendered correctly in every frame.
4. Model Synchronization: The update_model method ensures that the internal representation used by the solver matches the values currently displayed in the GUI cubes.
