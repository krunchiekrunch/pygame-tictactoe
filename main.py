import pygame
import random

pygame.init()

screen_width = 600
screen_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font = pygame.font.Font(None, 36)

# game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame tic tac toe!")

# board
board = [[' ' for _ in range(3)] for _ in range(3)]

player = 'X'
game_over = False

# drawing on board
def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, black, (i * 200, 0), (i * 200, 600), 2)
        pygame.draw.line(screen, black, (0, i * 200), (600, i * 200), 2)

# draw symbols
def draw_symbols():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, red, (col * 200 + 20, row * 200 + 20), (col * 200 + 180, row * 200 + 180), 5)
                pygame.draw.line(screen, red, (col * 200 + 180, row * 200 + 20), (col * 200 + 20, row * 200 + 180), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, blue, (col * 200 + 100, row * 200 + 100), 80, 5)

# check who won
def check_win(player):
    # rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    # diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

# check for a draw
def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

# ai playing
def ai_move():
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 'X':
            x, y = pygame.mouse.get_pos()
            row = y // 200
            col = x // 200
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player = 'O'

    if not game_over and player == 'O':
        ai_move()
        player = 'X'

    screen.fill(white)
    draw_board()
    draw_symbols()

    if check_win('X'):
        print('X(You) won! Congratulations!')
        game_over = True
    elif check_win('O'):
        print('O(Bot) won! Better luck next time.')
        game_over = True
    elif check_draw():
        print('Draw! Better luck next time.')
        game_over = True

    pygame.display.update()

pygame.quit()
