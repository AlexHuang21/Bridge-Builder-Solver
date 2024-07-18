# Bridge-Builder-Solver
Alex Huang

### Introduction <br>
This project implements a solver for the puzzle game Hashiwokakero, also known "Bridges" or "Hashi". The solver reads a rectangular grid containing islands represented by numbers and empty spaces represented by dots. The goal is to connect all the islands with a network of bridges following specific rules: bridges must run horizontally or vertically, not cross each other or islands, have no more than three bridges between any pair of islands, and the total number of bridges connected to each island must match the number on the island.

### Features <br>
- Grid Parsing: Reads the input grid from standard input and initializes the puzzle's internal representation.
- Bridge Validation: Ensures bridges are placed correctly, adhering to game rules.
- Backtracking Algorithm: Uses a backtracking approach to explore possible solutions and validate them.
- Solution Output: Outputs one valid solution if multiple exist, displaying the grid with bridges in place.
- Dynamic Updates: Handles dynamic updates to the puzzle state, ensuring real-time correctness checks.

### Implementation Details <br>
The solver initializes by reading the puzzle grid, parsing island values, and setting up the board. It employs a backtracking algorithm to explore possible placements of bridges, ensuring all constraints are met. The solution is verified by checking if the total number of bridges matches the island values. The program prints the solution in a readable format, with different characters representing single, double, and triple bridges.

### How to Run <br>
- Prepare Input Grid: Create a text file containing the puzzle grid.
- Run the Solver: Use the following command:

python3 hashi.py < input.txt

- View Solution: The program will output the grid with bridges if a solution is found.

### Topics Covered <br>
- Backtracking Algorithms
- Constraint Satisfaction Problems
- Grid and Graph Data Structures
- Dynamic Programming
- Input/Output Handling in Python

Explore the code to understand the algorithms and data structures used!
