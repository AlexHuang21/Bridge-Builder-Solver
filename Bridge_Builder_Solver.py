import sys

# Define a class to represent the Hashi puzzle solver
class HashiSolver:
    def __init__(self):
        self.puzzle = [['' for _ in range(40)] for _ in range(40)]
        self.solution = [[(0, 0) for _ in range(40)] for _ in range(40)]
        self.bridges = []
        self.num_rows = 1
        self.num_cols = 1

    def is_valid_move(self, row, col, dir, planks):
        new_row, new_col = row, col
        if dir == 0:
            new_col += 1
        elif dir == 1:
            new_row += 1
        elif dir == 2:
            new_col -= 1
        elif dir == 3:
            new_row -= 1

        if not (0 <= new_row < self.num_rows and 0 <= new_col < self.num_cols):
            return False

        island_value = 0
        if self.puzzle[row][col].isdigit():
            island_value = int(self.puzzle[row][col])
        elif self.puzzle[row][col] in ['a', 'b', 'c']:
            island_value = ord(self.puzzle[row][col]) - ord('a') + 10

        if (self.puzzle[new_row][new_col] == '.' and
                self.solution[new_row][new_col][0] + planks <= island_value):
            return True
        return False

    def is_solution(self):
        for bridge in self.bridges:
            row1, col1, row2, col2 = *bridge[0], *bridge[1]
            if (self.solution[row1][col1][0] + self.solution[row2][col2][0] !=
                    int(self.puzzle[row1][col1])):
                return False
        return True

    def backtrack(self, bridge_index):
        if bridge_index == len(self.bridges):
            if self.is_solution():
                print("Solution:")
                self.print_solution()
                sys.exit(0)
            return

        for planks in range(4):
            row1, col1, row2, col2 = *self.bridges[bridge_index][0], *self.bridges[bridge_index][1]
            dir1, dir2 = (0, 2) if col1 == col2 else (1, 3)

            if (self.is_valid_move(row1, col1, dir1, planks) and
                    self.is_valid_move(row2, col2, dir2, planks)):
                # Implement the logic to update the solution state before and after recursive calls
                pass  # This part is omitted for brevity

    def create_puzzle(self):
        for line in sys.stdin:
            row, col = len(self.puzzle), 0
            for char in line.strip():
                self.puzzle[row][col] = char
                col += 1
            self.num_rows, self.num_cols = row + 1, col

    def print_puzzle(self):
        for i in range(self.num_rows):
            print(''.join(self.puzzle[i]))

    def print_solution(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                # Implement the logic to print the solution
                pass  # This part is omitted for brevity

    def solve(self):
        # Implement the logic to initialize the solving process
        pass  # This part is omitted for brevity

# Main function to run the solver
if __name__ == "__main__":
    solver = HashiSolver()
    solver.create_puzzle()
    solver.solve()
    print("No solution found.")
