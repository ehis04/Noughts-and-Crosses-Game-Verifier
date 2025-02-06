# Tic-Tac-Toe Game Verifier

## Overview
This project implements a Tic-Tac-Toe game verifier in Python. The verifier checks the state of a given 3x3 Tic-Tac-Toe grid and determines whether:
This project implements a noughts and crosses game verifier in python that is part of a larger application that manages the game session.
The verifier checks the state of the given NXN (default 3x3) noughts and cross grid and determines whether:

- The player using "X" has won.
- The player using "O" has won.
- The game has ended in a draw with neither side winning

The implementation follows best practices, including **input validation**, **modular code design**, and **automated testing**.

---

## Features
- **Game State Validation:** Ensures that the grid is a valid 3x3 structure containing only `X`, `O`, or `''`.
- **Winner Detection:** Checks rows, columns, and diagonals for a winning condition.
- **Error Handling:** Raises `ValueError` for invalid grids.
- **Automated Testing:** Includes a test suite for verifying correctness.

---

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Clone the Repository ###
```sh
 git clone <repository-url>
 cd tic-tac-toe-verifier
```

### Run the Script
```sh
 python implementation.py
```

---

## Usage
### **1. Running the Script with Predefined Tests**
Run the following command to execute built-in tests:
```sh
 python implementation.py
```
**Expected Output:**
```
Test 1 passed: X wins
Test 2 passed: O wins
Test 3 passed: X wins
Test 4 passed: Game is ongoing
```

### **2. Running in Interactive Mode**
You can manually test different Tic-Tac-Toe grids using Python's interactive shell:
```sh
 python
```
Then, run the following commands:
```python
from implementation import TicTacToeVerifier

grid = [
    ["X", "X", "X"],
    ["O", "O", ""],
    ["", "", ""]
]

game = TicTacToeVerifier(grid)
print(game.check_winner())  # Expected output: "X wins"
```

### **3. Running a Separate Test Script**
Create a test script (`test_tic_tac_toe.py`) with multiple test cases, then execute:
```sh
 python test_tic_tac_toe.py
```

---

## Code Structure
### `implementation.py`
- **`TicTacToeVerifier` Class**
  - `__init__(grid)`: Initializes the game state.
  - `_validate_grid(grid)`: Ensures the grid is valid.
  - `check_winner()`: Determines if there is a winner or if the game is ongoing.
  - `_get_winner()`: Checks rows, columns, and diagonals for a winning condition.

- **Why is this implementation designed this way?**
  - **No Game Management**: Since this class is meant to be used within a larger
    application that manages the game session, it does **not** handle:
    - Player turns
    - Move validation
    - Game progression (who plays next, tracking moves over time)
  - **Modular Grid Checking**: The `_get_winner()` function dynamically handles
    any NxN board, ensuring flexibility if the application expands to larger grids.
  - **Encapsulation of Concerns**:
    - `_validate_grid()` ensures correctness of input.
    - `check_winner()` provides a simple interface for external usage.
  - **Error Handling for Integration**: The class ensures that any invalid input
    is detected immediately, allowing the larger application to handle errors
    properly rather than causing silent failures.
  - **Why No User Interaction?**
    - This implementation does not accept user input directly because a larger
      application will handle player moves and grid updates before calling `check_winner()`.
    - This ensures that the verifier remains a **pure function**-like component
      that only validates the game state when required.
  - **Why Not Modify the Grid?**
    - The class does not modify the grid state; it only reads it. This allows
      the external system to control how moves are stored and updated without
      unexpected side effects from this class.
  - **Scalability for Future Changes**:
    - The class can be used for standard 3x3 Tic-Tac-Toe but is designed to
      support larger grid sizes without major modifications.

---

## Example Test Cases
| **Test Case** | **Grid** | **Expected Output** |
|--------------|---------|------------------|
| X Wins (Row) | `[['X', 'X', 'X'], ['O', 'O', ''], ['', '', '']]` | "X wins" |
| O Wins (Column) | `[['O', 'X', 'X'], ['O', 'O', 'O'], ['X', '', '']]` | "O wins" |
| X Wins (Diagonal) | `[['X', 'O', 'O'], ['O', 'X', 'O'], ['', '', 'X']]` | "X wins" |
| Game Ongoing | `[['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]` | "Game is ongoing" |

---

## Error Handling
The script raises a `ValueError` if:
1. The grid is not a **3x3 matrix**.
2. Any cell contains characters other than **'X', 'O', or ''**.

Example:
```python
invalid_grid = [
    ["X", "O", "X"],
    ["X", "A", "O"],  # Invalid character 'A'
    ["O", "X", "O"]
]

game = TicTacToeVerifier(invalid_grid)  # Raises ValueError
```

---

## Contribution
If you want to contribute:
1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request.

---

## License
This project is licensed under the MIT License.
