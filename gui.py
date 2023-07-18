import pygame
from sudoku import Sudoku

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 200)
LIGHT_BLUE = (100, 150, 230)
DARK_BLUE = (20, 70, 170)
ORANGE = (255, 165, 0)
FONT_COLOR = (50, 50, 50)
USER_VALUE_COLOR = (80, 80, 80)  # New color for the numbers entered by the user

# Define dimensions
WINDOW_SIZE = (540, 600)
GRID_SIZE = 9
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE
BUTTON_SIZE = (100, 40)

# Initialize pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Solver")

def draw_background():
    # Draw blue background
    window.fill(BLUE)

def draw_board(board, selected):
    draw_background()

    # Draw Sudoku grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            cell_color = LIGHT_BLUE if (i, j) != selected else ORANGE

            # Draw the rounded border for each cell
            pygame.draw.rect(window, cell_color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(window, DARK_BLUE, (x, y, CELL_SIZE, CELL_SIZE), 3)

            # Draw the numbers on the board
            font = pygame.font.SysFont("comicsans", 40)
            if board[i][j] != 0:
                number_color = FONT_COLOR if board[i][j] != 0 else USER_VALUE_COLOR
                number = font.render(str(board[i][j]), True, number_color)
                window.blit(number, (x + CELL_SIZE // 2 - number.get_width() // 2,
                                     y + CELL_SIZE // 2 - number.get_height() // 2))

    # Draw "Solve" button
    solve_button_rect = pygame.Rect(220, 560, *BUTTON_SIZE)
    pygame.draw.rect(window, ORANGE, solve_button_rect)
    font = pygame.font.SysFont("comicsans", 24)
    text = font.render("Solve", True, WHITE)
    window.blit(text, (solve_button_rect.centerx - text.get_width() // 2,
                       solve_button_rect.centery - text.get_height() // 2))

    pygame.display.update()

def main():
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    selected_cell = None
    solve_button = pygame.Rect(220, 560, *BUTTON_SIZE)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                selected_cell = (row, col)

                # Check if the "Solve" button is clicked
                if solve_button.collidepoint(x, y):
                    solver = Sudoku(board)
                    solved_board = solver.solve()
                    if solved_board:
                        board = solved_board
            if event.type == pygame.KEYDOWN:
                if selected_cell:
                    if event.unicode.isdigit() and int(event.unicode) in range(1, 10):
                        row, col = selected_cell
                        board[row][col] = int(event.unicode)

        draw_board(board, selected_cell)

    pygame.quit()

if __name__ == "__main__":
    main()
