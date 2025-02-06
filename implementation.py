"""
06/02/2025 Noughts and Crosses Game Verifier by Ehis Oghina.

This script implements a noughts and cross game verifier in Python. It evaluates the state if a given NXN noughts and crosses grid to determine whether:
-   The player using "X" has won
-   The player using "O" has won
-   The game ended in a draw with neither side winning

    As per instruction this script is designed to be used as part of a larger application that manages the game session for so it doesn't handle:
        -   player turns
        -   move validation
        -   game flow
    It simply verifies the current state of the board
"""

class Noughts_and_Crosses_Verifier:
    def __init__(self, grid, size=3):
        """
        Initialises the game verifier with a NXN grid(default 3x3).
        
        :paramater grid: List of lists representing the Noughts and Crosses board.
        :paramater size: The size of the grid (default: 3 for a 3x3 game).
        """

        # Checks the grid for validity before its stored
        self.size = size
        if not self._validate_grid(grid):
            raise ValueError(f"Invalid grid format. Must be {size}x{size} with only 'X', 'O', or ''.")
        self.grid = grid

    def _validate_grid(self, grid):
        """
        Validates that the grid is an NxN list of lists containing only 'X', 'O', or ''.
        - Ensures the grid is a proper NxN matrix.
        - Checks that every cell contains a valid character.
        """
        # Prevents incorrect input formats which would cause issues further down the line
        if not isinstance(grid, list) or len(grid) != 3: # Check that the grid is a list and has correct dimensions
            return False
        for row in grid:
            if not isinstance(row, list) or len(row) != 3: # Make sure each row is a list with correct size
                return False
            if any(cell not in ('X', 'O', '') for cell in row): # Ensure each cell contains only valid characters
                return False
        return True # If all checks pass, the grid is valid

    def check_winner(self):
        """
        Checks the state of the game and returns:
        - "X wins" if X has won.
        - "O wins" if O has won.
        - "Draw" if no one has won yet.
        Calls the `_get_winner()` function to determine the game outcome.
        """
        winner = self._get_winner()
        return f"{winner} wins" if winner else "Draw"

    def _get_winner(self): # Function reads from grid, doesn't perform any modification
        """
        Checks for a winning condition in rows, columns, and diagonals.
        Returns 'X' or 'O' if a winner is found, otherwise None.
        
        - Iterates through rows and columns to check for a complete match.
        - Checks both diagonals to determine if all values match for a win.
        """
        # Check rows and columns
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != "":
                return self.grid[i][0] # Row match
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != "":
                return self.grid[0][i] # Column match

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != "":
            return self.grid[0][0] # Primary diagonal match
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != "":
            return self.grid[0][2] # Secondary diagonal match

        return None # No result found


def run_tests():
    """Runs a set of test cases to verify the correctness of the game verifier."""
    test_cases = [
        ([  # X wins (row)
            ["X", "X", "X"],
            ["O", "O", ""],
            ["", "", ""]
        ], "X wins"),
        
        ([  # O wins (column)
            ["O", "X", "X"],
            ["O", "O", "O"],
            ["X", "", ""]
        ], "O wins"),
        
        ([  # X wins (diagonal)
            ["X", "O", "O"],
            ["O", "X", "O"],
            ["", "", "X"]
        ], "X wins"),
        
        ([  # Draw
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ], "Draw")
    ]
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        try:
            from implementation import Noughts_and_Crosses_Verifier  
            game = Noughts_and_Crosses_Verifier(grid)
            result = game.check_winner()
            assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
            print(f"Test {i} passed: {result}")
        except ValueError as e:
            print(f"Test {i} failed: {e}")

if __name__ == "__main__":
    run_tests()