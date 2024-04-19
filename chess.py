import pygame
import sys
import os
from random import randint
#initializing values
Dimensions = 8
whidth = 400
height = 400
sq_size = whidth // 8
size = sq_size // 1.3

#initializing screen
screen = pygame.display.set_mode((whidth, height))
pygame.display.set_caption("Chess game")
# pygame.display.set_icon(pygame.image.load('photos/icon.png'))

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
first_hod = 'white'
def white_or_black():
    global first_hod
    first_hod = "black" if first_hod == "white" else 'white'


sqSelected = ()  # Текущий выбранный квадрат
PlayerClick = []  # Список для хранения кликов игрока

def move_chess(event, end_pos):
    global sqSelected, PlayerClick, white_pieces, black_pieces, first_hod
    
    row, col = event
    sq_row = row // sq_size
    sq_col = col // sq_size
    pos_g = (sq_col, sq_row)
    print(pos_g)
    end_row, end_col = end_pos
    esq_row = end_row // sq_size
    esq_col = end_col // sq_size
    new_pos = (esq_col, esq_row)
    print(new_pos)

    
    if len(PlayerClick) == 0:  # Если это первый клик
        sqSelected = (sq_col, sq_row)  # Фиксируем текущий выбранный квадрат
        PlayerClick.append(new_pos)  # Добавляем позицию в список кликов игрока
    else:  # Если это второй клик
        # Перемещаем фигуру на новое место
        move_piece(PlayerClick[0], new_pos)
        # Сбрасываем выбранный квадрат и список кликов игрока
        sqSelected = ()
        PlayerClick = []

def move_piece(start_pos, end_pos):
    global white_pieces, black_pieces, first_hod
    
    if first_hod == "white":
        figure = white_pieces
        enemy_pieces = black_pieces
    else:
        figure = black_pieces
        enemy_pieces = white_pieces
    
    # Проверяем, есть ли фигура на стартовой позиции
    for piece_type in figure:
        if start_pos in figure[piece_type]:
            print("some")
            # Если фигура найдена, перемещаем ее на новую позицию
            figure[piece_type][figure[piece_type].index(start_pos)] = end_pos
            # Если фигура переместилась на позицию вражеской фигуры, удаляем вражескую фигуру
            for enemy_piece_type in enemy_pieces:
                if end_pos in enemy_pieces[enemy_piece_type]:
                    enemy_pieces[enemy_piece_type].remove(end_pos)
            break




run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            white_or_black()
            col = mouse_pos[0] // sq_size
            row = mouse_pos[1] // sq_size
            if sqSelected == (row, col):
                sqSelected = ()
                PlayerClick = []
            else:
                sqSelected = (row, col)
                PlayerClick.append(sqSelected)

        elif event.type == pygame.MOUSEBUTTONUP:
            if len(PlayerClick) == 1:
                end_pos = pygame.mouse.get_pos()
                move_chess(mouse_pos, end_pos)

        # elif event.type == pygame.MOUSEBUTTONUP:
        #     end_pos = pygame.mouse.get_pos()
        #     # move_chess(mouse_pos)
        #     # white_or_black()
        #     col = end_pos[0] // sq_size
        #     row = end_pos[1]//sq_size
        #     if sqSelected == (row, col):
        #         sqSelected = ()
        #         PlayerClick = []
        #     else:

        #         sqSelected = (row, col)
        #         PlayerClick.append(sqSelected)
        #     if len(PlayerClick) == 2:
        #         pass
        #     move_chess(end_pos)


    draw_board()
    draw_pieces()
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
