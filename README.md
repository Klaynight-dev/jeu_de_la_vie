# Conway's Game of Life in Python

This Python program implements Conway's Game of Life with a Tkinter graphical interface. The Game of Life is a cellular automaton that evolves based on given initial states and simple rules.

## Features

### Cell
- The `Cell` class represents a cell within the game grid.
- Each cell can be either dead (`False`) or alive (`True`).
- Available methods: `is_alive()`, `die()`, `birth()`.

### Grid
- The `Grid` class represents the game grid.
- Initializes a grid with a given size and initial configuration.
- Counts the number of living neighbors for each cell.
- Updates the grid state according to the rules of the Game of Life.

### GameOfLifeGUI
- Graphical interface created with Tkinter to display the game grid.
- Creates a window with a canvas to display the grid.
- Updates the graphical display at each iteration of the simulation.

## Usage
1. Ensure Python is installed.
2. Run the program using `python main.py`.
3. A window opens displaying the initial grid.
4. The simulation starts and evolves according to the rules of the Game of Life.
5. Living cells are shown in black, dead cells in white.

## Files
- `main.py`: Contains the `Cell`, `Grid`, and `GameOfLifeGUI` classes.
- `seed.py`: Functions for generating a random initial configuration.

## Note
This code implements Conway's rules for the Game of Life. The grid is updated at each iteration, changing the state of the cells based on their neighborhood. The initial grid configuration is generated randomly.
