# Commit 1: Initial setup with pygame window and imports
import pygame
import time
from random import randint

pygame.font.init()


# Commit 2: Create Grid class and initialize board
class Grid:
    board = [
        [7, 8, 0, 5, 0, 4, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 0, 0],
        [0, 4, 0, 7, 8, 0, 0, 3, 0],
        [6, 9, 0, 2, 0, 7, 8, 0, 0],
        [0, 0, 8, 0, 4, 0, 3, 0, 0],
        [0, 0, 2, 8, 0, 9, 0, 5, 7],
        [0, 5, 0, 0, 7, 2, 0, 4, 0],
        [0, 0, 0, 0, 5, 0, 9, 0, 0],
        [0, 0, 0, 1, 0, 3, 0, 8, 5],
    ]

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols

        # Commit 3: Initialize cubes (cells)
        self.cubes = [
            [Cube(self.board[i][j], i, j, width, height) for j in range(cols)]
            for i in range(rows)
        ]

        self.width = width
        self.height = height
        self.model = None
        self.update_model()

        self.selected = None
        self.win = win

    # Commit 4: Update internal board model
    def update_model(self):
        self.model = [
            [self.cubes[i][j].value for j in range(self.cols)]
            for i in range(self.rows)
        ]

    # Commit 5: Place value with validation
    def place(self, val):
        row, col = self.selected

        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)) and self.solve():
                return True
            else:
                self.cubes[row][col].set(0)
                self.update_model()
                return False

    # Commit 6: Sketch temporary number
    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    # Commit 7: Draw grid lines and board
    def draw(self):
        gap = self.width / 9

        for i in range(self.rows + 1):
            thick = 4 if i % 3 == 0 else 1

            pygame.draw.line(self.win, (0, 0, 0),
                             (0, i * gap), (self.width, i * gap), thick)

            pygame.draw.line(self.win, (0, 0, 0),
                             (i * gap, 0), (i * gap, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    # Commit 8: Cell selection logic
    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    # Commit 9: Clear cell
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    # Commit 10: Mouse click handler
    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        return None

    # Commit 11: Check if board is complete
    def is_finished(self):
        for row in self.model:
            if 0 in row:
                return False
        return True

    # Commit 12: Backtracking solver
    def solve(self):
        find = find_empty(self.model)
        if not find:
            return True

        row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i

                if self.solve():
                    return True

                self.model[row][col] = 0

        return False


# Commit 13: Cube class (individual cell)
class Cube:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    # Commit 14: Draw numbers in cell
    def draw(self, win):
        fnt = pygame.font.SysFont("verdana", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value != 0:
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + 20, y + 15))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


# Commit 15: Find empty cell
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


# Commit 16: Validation logic
def valid(bo, num, pos):
    row, col = pos

    if num in bo[row]:
        return False

    for i in range(9):
        if bo[i][col] == num:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num:
                return False

    return True


# Commit 17: Main game loop
def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Solver")

    board = Grid(9, 9, 540, 540, win)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((255, 255, 255))
        board.draw()
        pygame.display.update()


main()
pygame.quit()
