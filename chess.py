import pygame
import sys
import os
from random import randint
from const import *


pygame.init()

pygame.display.set_caption("Chess game")



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
first_hod = 'black'
def white_or_black():
    global first_hod
    first_hod = "white" if first_hod == "black" else 'black'


sqSelected = ()  # Текущий выбранный квадрат
PlayerClick = []  # Список для хранения кликов игрока

def move_chess(event, end_pos):
    global sqSelected, PlayerClick, white_pieces, black_pieces, first_hod
    
    row, col = event
    sq_row = row // sq_size
    sq_col = col // sq_size
    pos_g = (sq_col, sq_row)
    # print(pos_g)
    end_row, end_col = end_pos
    esq_row = end_row // sq_size
    esq_col = end_col // sq_size
    new_pos = (esq_col, esq_row)
    # print(new_pos)

    
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
    
    if first_hod == "black":
        figure = white_pieces
        enemy_pieces = black_pieces
    else:
        figure = black_pieces
        enemy_pieces = white_pieces
        
    for type_piece in figure:

        figure_type = figure["pawn"]
        if start_pos in figure_type:



            if first_hod == "black":
                

                if end_pos == (start_pos[0]-2, start_pos[1]) or end_pos == (start_pos[0]-1, start_pos[1]):
                    
                    if end_pos in black_pieces["pawn"]:
                        
                        print("yes")
                        
                    else:
                        
                        figure_type[figure_type.index(start_pos)] = end_pos
                    
                elif end_pos == (start_pos[0] - 1, start_pos[1] - 1) or end_pos == (start_pos[0] - 1, start_pos[1] + 1):
                    print((start_pos[0] - 1, start_pos[1] - 1), (start_pos[0] - 1, start_pos[1] + 1))
                    # Проверяем, находится ли на конечной позиции фигура противоположного цвета
                    for enemy_piece_type in enemy_pieces:
                        if end_pos in enemy_pieces[enemy_piece_type]:
                            # Если да, то совершаем удар и удаляем фигуру противоположного цвета
                            figure_type[figure_type.index(start_pos)] = end_pos
                            enemy_pieces[enemy_piece_type].remove(end_pos)
                            break
                    
            else:
                
                if end_pos == (start_pos[0]+2, start_pos[1]) or end_pos == (start_pos[0]+1, start_pos[1]):
                    
                    if end_pos in white_pieces["pawn"]:
                        
                        pass              
                    else:
                        
                        figure_type[figure_type.index(start_pos)] = end_pos

                    
                elif end_pos == (start_pos[0] + 1, start_pos[1] - 1) or end_pos == (start_pos[0] + 1, start_pos[1] + 1):
                # Проверяем, находится ли на конечной позиции фигура противоположного цвета
                    for enemy_piece_type in enemy_pieces:
                        if end_pos in enemy_pieces[enemy_piece_type]:
                            # Если да, то совершаем удар и удаляем фигуру противоположного цвета
                            figure_type[figure_type.index(start_pos)] = end_pos
                            enemy_pieces[enemy_piece_type].remove(end_pos)
                            break

        else:
            pass




run_game = True
while run_game:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
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
                white_or_black()
                end_pos = pygame.mouse.get_pos()
                move_chess(mouse_pos, end_pos)
        elif event.type == pygame.K_DOWN:
            print("hello")
            white_or_black()

       

    screen.fill((255,255,255))
    draw_board()
    draw_pieces()
    # screen.fill((0,0,0))
    font = pygame.font.Font(None, 40)
    text = font.render(f"turn: {first_hod}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(800-100, 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    
pygame.quit()
sys.exit()
