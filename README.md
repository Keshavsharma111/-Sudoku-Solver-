# -Sudoku-Solver-
 Sudoku Solver  use Python ,pygame
# Sudoku Solver (Pygame)

A GUI-based Sudoku solver built using Python and Pygame.

## Features
- Interactive Sudoku board
- Backtracking solver
- Visual solving animation
- Timer and mistake counter

## Controls
- Click: Select cell
- Number keys: Input value
- Enter: Confirm value
- Space: Auto solve
- Delete: Clear cell

## Installation
pip install pygame

## Run
python main.py

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/0c76af4d-84f4-47f4-abd6-2d62d19a1ee0" />


## 📊 Project Commit Flow

```mermaid
graph TD;

A[Initial Setup<br>Setup pygame window] --> B[Grid & Cube Classes<br>Board UI rendering]
B --> C[Draw Grid Lines<br>3x3 box borders]
C --> D[Render Numbers<br>Display values]
D --> E[User Interaction<br>Mouse & keyboard input]
E --> F[Validation Logic<br>Sudoku rules check]
F --> G[Backtracking Solver<br>Recursive solution]
G --> H[GUI Solver Animation<br>Step-by-step solving]
H --> I[Timer & Strikes<br>Game features]
I --> J[Final Cleanup<br>Refactor & polish]

