# NRK Former Solver

A Python program to solve shape-matching puzzles by removing connected groups and applying gravity. The solver uses a heuristic-based approach with a priority queue (A* search) to find an optimal sequence of moves.

## Features

- Identifies connected groups of the same symbol in a 2D board.
- Removes selected groups and applies gravity to collapse remaining shapes.
- Uses a heuristic function to prioritize optimal moves.
- Implements A* search for efficient problem-solving.
- Prints the step-by-step solution, including board states.

## How It Works

1. The program initializes with a predefined board where numbers represent different shapes.
2. It searches for connected groups of the same shape.
3. If a group is removed, the shapes above it fall down (gravity effect).
4. The algorithm attempts to solve the board in an optimal number of moves.
5. The final solution is displayed, showing each step.

## Code Overview

- `get_connected_shapes(board, x, y)`: Finds all connected tiles of the same type.
- `remove_shapes(board, connected)`: Removes the selected shapes by setting them to `0`.
- `apply_gravity(board)`: Moves shapes downward to fill empty spaces.
- `heuristic(board)`: Calculates a heuristic score based on connected components.
- `solve_board(board, max_depth=13)`: Uses A* search to find the optimal move sequence.
- `print_board(board)`: Prints the board for debugging.

## Run Code
Write in console: `python3 former.py`
