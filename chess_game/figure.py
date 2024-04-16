import pygame
import sys
import os
from random import randint

Dimensions = 8
whidth = 400
height = 400
sq_size = whidth // 8
size = sq_size // 1.3

screen = pygame.display.set_mode((whidth, height))
pygame.display.set_caption("Chess game")
pygame.display.set_icon(pygame.image.load('photos/icon.png'))

# Define colors
white = pygame.Color(250, 218, 95)
black = pygame.Color(0, 0, 0)
grey = pygame.Color(150, 75, 0)

# Load images dynamically
image_folder = 'photos'

pieces = ['pawn', 'horse', 'rook', 'bishop', 'king', 'queen']
colors = ['white','black']
black_pieces = {
    'queen': [(0, 3)],
    'king':[(0, 4)], 
    "bishop" :[(0, 2), (0, 5)], 
    "rook": [(0,0), (0, 7)],
    "horse":[(0, 1), (0, 6)],
    "pawn":[(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
}

white_pieces = {
    'queen': [(7, 3)],
    'king': [(7, 4)], 
    "bishop": [(7, 2), (7, 5)], 
    "rook": [(7, 0), (7, 7)],
    "horse": [(7, 1), (7, 6)],
    "pawn": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)]
}

images = {}
for color in colors:
    for piece in pieces:
        img_path = os.path.join(image_folder, color, f"{color}_{piece}.png")
        img = pygame.transform.scale(pygame.image.load(img_path), (size, size))
        images[f"{color}_{piece}"] = img

def draw_board():
    for i in range(Dimensions):
        for j in range(0, Dimensions):
            if (i + j) % 2 == 0:
                color = white
            else:
                color = grey
            pygame.draw.rect(screen, color, pygame.Rect(j * sq_size, i * sq_size, sq_size, sq_size))

def draw_pieces():
    for color in colors:
        if color == "black":
            for piece_type, positions in black_pieces.items():
                for pos in positions:
                    x, y = pos
                    screen.blit(images[f"{color}_{piece_type}"], (y * sq_size + sq_size // 10, x * sq_size + sq_size // 10))
        if color == "white":
            for piece_type, positions in white_pieces.items():
                for pos in positions:
                    x, y = pos
                    screen.blit(images[f"{color}_{piece_type}"], (y * sq_size + sq_size // 10, x * sq_size + sq_size // 10))

def get_piece_at_mouse_position(mouse_pos):
    for color in colors:
        for piece_type, positions in black_pieces.items() if color == "black" else white_pieces.items():
            for pos in positions:
                x, y = pos
                if (y * sq_size + sq_size // 10 <= mouse_pos[0] <= y * sq_size + sq_size // 10 + size) and (x * sq_size + sq_size // 10 <= mouse_pos[1] <= x * sq_size + sq_size // 10 + size):
                    print(color, piece_type, pos)
                    return (color, piece_type, pos)
                
    return None

def get_square_at_mouse_position(mouse_pos):
    row = mouse_pos[1] // sq_size
    col = mouse_pos[0] // sq_size
    print(row, col)
    return (row, col)


def valid_move(selected_piece, event, current_player):
    color, piece_type, old_position = selected_piece
    mouse_x, mouse_y = event
    
    sq_x = mouse_x // sq_size
    sq_y = mouse_y // sq_size
    print(sq_y, sq_x)
    if (color == current_player):  # Убеждаемся, что фигура принадлежит текущему игроку
        if piece_type == "pawn":
            if color == "white":
                if old_position[0] == 6:  # Если это первый ход белой пешки
                    if sq_x == old_position[1] and (sq_y == old_position[0] - 1 or sq_y == old_position[0] - 2):
                        old_position[0] = old_position[0]-2
                        return True
                else:  # Если это не первый ход белой пешки
                    if sq_x == old_position[1] and sq_y == old_position[0] - 1:
                        return True
            elif color == "black":
                if old_position[0] == 1:  # Если это первый ход черной пешки
                    if sq_x == old_position[1] and (sq_y == old_position[0] + 1 or sq_y == old_position[0] + 2):
                        return True
                else:  # Если это не первый ход черной пешки
                    if sq_x == old_position[1] and sq_y == old_position[0] + 1:
                        return True
    return False

current_player = 'white'
def switch_player():
    global current_player
    current_player = 'black' if current_player == 'white' else 'white'


def move_piece(selected_piece, destination_square):
    global current_player
    color, piece_type, old_position = selected_piece
    new_x, new_y = destination_square
    if color == "black":
        new_positions = [(x, y) for x, y in black_pieces[piece_type] if (x, y) != old_position]  # Remove old position
        
        new_positions.append((new_x, new_y))  # Add new position
        print(f"new pos {new_positions}")
        black_pieces[piece_type] = new_positions
        print(black_pieces)
    else:
        new_positions = [(x, y) for x, y in white_pieces[piece_type] if (x, y) != old_position]  # Remove old position
        new_positions.append((new_x, new_y))  # Add new position
        white_pieces[piece_type] = new_positions
        print(f"hi {white_pieces}")



    if destination_square in black_pieces.values() or destination_square in white_pieces.values():
        if current_player == 'white':
            for piece_type, positions in black_pieces.items():
                if destination_square in positions:
                    del black_pieces[piece_type]
        elif current_player == 'black':
            for piece_type, positions in white_pieces.items():
                if destination_square in positions:
                    del white_pieces[piece_type]

# Начальный игрок


run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected_piece = get_piece_at_mouse_position(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_piece is not None:
                mouse_pos = pygame.mouse.get_pos()
                destination_square = get_square_at_mouse_position(mouse_pos)
                if valid_move(selected_piece, mouse_pos, current_player):  # Передаем текущего игрока в функцию valid_move
                    move_piece(selected_piece, destination_square)
                    switch_player()
                selected_piece = None

    draw_board()
    draw_pieces()
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
