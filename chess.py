import pygame
import sys
import os
from const import *
from figure import record_audio_and_recognize
from test2 import voise
import time
pygame.init()

pygame.display.set_caption("Chess game")


#initialised a values
image_folder1 = '/Users/drake/Desktop/vscode/oshi/progect/photos/type1'
image_folder2 = "/Users/drake/Desktop/vscode/oshi/progect/photos/type2"
image_folder3 = "/Users/drake/Desktop/vscode/oshi/progect/photos/type3"
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




red = pygame.Color(255, 0, 0)

    

images = {}
for color in colors:
    for piece in pieces:
        img_path = os.path.join(image_folder1, color, f"{color}_{piece}.png")
        img = pygame.transform.scale(pygame.image.load(img_path), (size, size))
        images[f"{color}_{piece}"] = img

images2 = {}
for color in colors:
    for piece in pieces:
        img_path = os.path.join(image_folder2, color, f"{piece}{color[0].upper()}.png")
        img = pygame.transform.scale(pygame.image.load(img_path), (size, size))
        images2[f"{piece}{color[0].upper()}"] = img

images3 = {}
for color in colors:
    for piece in pieces:
        img_path = os.path.join(image_folder3, color, f"{color}_{piece}.PNG")
        img = pygame.transform.scale(pygame.image.load(img_path), (size, size))
        images3[f"{color}_{piece}"] = img

button_wight = 200
button_height = 70
button_x, button_y = 600, 350


font = pygame.font.Font(None, 20)

def draw_button():
    pygame.draw.rect(screen, (23, 100, 200), (button_x, button_y, button_wight, button_height))
    text = font.render("switch skin", True, (0,0,0))
    text_position = text.get_rect(center= (800-100, 400))
    screen.blit(text, text_position)

def draw_board(selected_sq):
    for i in range(Dimensions):
        for j in range(0, Dimensions):
            if (i + j) % 2 == 0:
                color = white
            else:
                color = black
            if (i, j) == selected_sq:
                color = red
            pygame.draw.rect(screen, color, pygame.Rect(j * sq_size, i * sq_size, sq_size, sq_size))
            if i == 0:  # Если это первая строка
                # Рисуем буквы для обозначения столбцов в правом верхнем углу
                font = pygame.font.Font(None, 36)
                text_color = black if (i + j) % 2 == 0 else white  # Чередуем цвета белый и черный
                text_surface = font.render(str(j+1), True, text_color)
                screen.blit(text_surface, (j * sq_size + sq_size - 16, 0))  # Отступ от верхнего края
            if j == 0:  # Если это первый столбец
                # Рисуем цифры для обозначения строк в левом нижнем углу
                font = pygame.font.Font(None, 36)
                text_color = black if (i + j) % 2 == 0 else white  # Чередуем цвета белый и черный
                text_surface = font.render(chr(97 + i), True, text_color)
                screen.blit(text_surface, (3, i * sq_size + sq_size - 70))  # Отступ от левого края
            # chr(97 + j)
            # Добавление буквенной нумерации столбцов
            if i == 0:  
                font = pygame.font.Font(None, 36)
                text_color = white if (i + j) % 2 == 0 else black  # Чередуем цвета белый и черный
                text_surface = font.render(str(i+1), True, text_color)
                screen.blit(text_surface, (j * sq_size + 10, i * sq_size + 10))  # Отступ для отображения букв          


def draw_pieces1():
    for color in colors:
        if color == "black":
            for piece_type, positions in black_pieces.items():
                for pos in positions:
                    x, y = pos
                    screen.blit(images3[f"{color}_{piece_type}"], (y * sq_size + sq_size // 10, x * sq_size + sq_size // 10))
        if color == "white":
            for piece_type, positions in white_pieces.items():
                for pos in positions:
                    x, y = pos
                    screen.blit(images3[f"{color}_{piece_type}"], (y * sq_size + sq_size // 10, x * sq_size + sq_size // 10))

def draw_pieces2():
    for color in colors:
        if color == "black":
            for piece_type, positions in black_pieces.items():
                for pos in positions:
                    x, y = pos
                    screen.blit(images2[f"{piece_type}{color[0].upper()}"], (y * sq_size + sq_size // 10, x * sq_size + sq_size // 10))
        if color == "white":
            for piece_type, positions in white_pieces.items():
                for pos in positions:
                    x, y = pos
                    screen.blit(images2[f"{piece_type}{color[0].upper()}"], (y * sq_size + sq_size // 10, x * sq_size + sq_size // 10))
first_hod = 'white'
def white_or_black():
    global first_hod
    first_hod = "black" if first_hod == "white" else 'white'


sqSelected = ()  # Текущий выбранный квадрат
PlayerClick = []  # Список для хранения кликов игрока


class InvalidMoveError(Exception):
    pass


def move_chess(event, end_pos):
    global sqSelected, PlayerClick, white_pieces, black_pieces, first_hod
    #start position
    print("end pos --> ", end_pos)
    row, col = event
    

    #end position
    end_row, end_col = end_pos
    print(f"end row --> {end_row}\n end col {end_col}")
    # esq_row = end_row // sq_size
    # esq_col = end_col // sq_size
    new_pos = (end_row, end_col)
    print("new pos --> ", new_pos)

    

    
    if len(PlayerClick) == 0:  # Если это первый клик
        sqSelected = (col, row)  # Фиксируем текущий выбранный квадрат
        PlayerClick.append(new_pos)  # Добавляем позицию в список кликов игрока
        
    else:  # Если это второй клик
        # Перемещаем фигуру на новое место

        move_piece(PlayerClick[0], new_pos)
        # Сбрасываем выбранный квадрат и список кликов игрока
        sqSelected = ()
        PlayerClick = []

def compare_list():
    global black_pieces, white_pieces
    all_pieces = []
    
    for b_value in black_pieces.values():
        for v in b_value:
            all_pieces.append(v)
    # print(black_pieces)
    
    for w_value in white_pieces.values():
        for w in w_value:
            all_pieces.append(w)
    return all_pieces


def move_piece(start_pos, end_pos):
    global white_pieces, black_pieces, first_hod
    global text, text_rect
    global lists_of_black, lists_of_white
    
    if first_hod == "black":
        figure = white_pieces
        enemy_pieces = black_pieces
    else:
        figure = black_pieces
        enemy_pieces = white_pieces
        
    for _ in figure:

        
        figure_type = figure["pawn"]
        if start_pos in figure_type:



            if first_hod == "black":
                

                if start_pos[0] == 6 and end_pos == (start_pos[0]-2, start_pos[1]) or end_pos == (start_pos[0]-1, start_pos[1]):
                    
                    
                    all_pieces = compare_list()

                    if end_pos in all_pieces:
                        white_or_black()
                    else:
                        figure_type[figure_type.index(start_pos)] = end_pos
                    
                elif end_pos == (start_pos[0] - 1, start_pos[1] - 1) or end_pos == (start_pos[0] - 1, start_pos[1] + 1):
                    
                    # print((start_pos[0] - 1, start_pos[1] - 1), (start_pos[0] - 1, start_pos[1] + 1))
                    # Проверяем, находится ли на конечной позиции фигура противоположного цвета
                    for enemy_piece_type in enemy_pieces:
                        if end_pos in enemy_pieces[enemy_piece_type]:
                            # Если да, то совершаем удар и удаляем фигуру противоположного цвета
                            figure_type[figure_type.index(start_pos)] = end_pos
                            enemy_pieces[enemy_piece_type].remove(end_pos)
                            break
                

            else:
                
                
                if start_pos[0] == 1 and end_pos == (start_pos[0]+2, start_pos[1]) or end_pos == (start_pos[0]+1, start_pos[1]):
                    all_pieces = compare_list()
                    # print(lists_of_white)
                    
                    if end_pos in all_pieces:
                        white_or_black()
                        # pass              
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
        
        correct_move = False
        figure_horse = figure["horse"]

        if start_pos in figure_horse:
            print(first_hod)
            if first_hod == "black":

                if (end_pos == (start_pos[0]-2, start_pos[1]-1) or end_pos == (start_pos[0]-2, start_pos[1]+1) or 
                    end_pos == (start_pos[0]+2, start_pos[1]-1) or end_pos == (start_pos[0]+2, start_pos[1]+1) or
                    end_pos == (start_pos[0]-1, start_pos[1]+2) or end_pos == (start_pos[0]+1, start_pos[1]+2) or
                    end_pos == (start_pos[0]-1, start_pos[1]-2) or end_pos == (start_pos[0]+1, start_pos[1]-2)):
                    print("correct white hod")
                    # print(end_pos)
                    # print("___")
                    # print((start_pos[0]-2, start_pos[1]-1))
                    # print("---")
                    # print(figure_horse)
                    
                    if end_pos not in black_pieces.values():
                        
                        all_pieces = compare_list()
                        if end_pos in all_pieces:
                            # await asyncio.sleep(0.5)
                            
                            for enemy_piece_type in enemy_pieces:

                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    # white_or_black()
                                    
                                    
                                    figure_horse[figure_horse.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    # correct_move = True
                                    break
                        
                               

                                
                        else:
                            # white_or_black()
                            
                            figure_horse[figure_horse.index(start_pos)] = end_pos
                    else:
                        
                        white_or_black()
                        # figure_horse[figure_horse.index(start_pos)] = end_pos
                else:
                    print("blacknon correct path")
                    first_hod = "white" if first_hod == "black" else "white"
                    first_hod = "black" if first_hod == "white" else "black"
                    # first_hod = "white" if first_hod == "black" else "white"
                    
                    
            else:
                
                if (end_pos == (start_pos[0]-2, start_pos[1]-1) or end_pos == (start_pos[0]-2, start_pos[1]+1) or 
                    end_pos == (start_pos[0]+2, start_pos[1]-1) or end_pos == (start_pos[0]+2, start_pos[1]+1) or
                    end_pos == (start_pos[0]-1, start_pos[1]+2) or end_pos == (start_pos[0]+1, start_pos[1]+2) or
                    end_pos == (start_pos[0]-1, start_pos[1]-2) or end_pos == (start_pos[0]+1, start_pos[1]-2)):
                    print("correct black hod")
                    if end_pos not in white_pieces.values():
                        
                        

                        all_pieces = compare_list()
                        # white_or_black()
                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    # Если да, то совершаем удар и удаляем фигуру противоположного цвета
                                    # white_or_black()
                                    figure_horse[figure_horse.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    # correct_move = True
                                    break
                                # correct_move = True
                            
                                
                            # white_or_black()
                                    
                                    
                                # Если на конечной позиции нет фигуры противоположного цвета, просто совершаем ход
                                    # figure_horse[figure_horse.index(start_pos)] = start_pos
                        else:
                            
                            # print("no")
                            # white_or_black()
                            # Если на конечной позиции нет фигуры противоположного цвета, просто совершаем ход
                            figure_horse[figure_horse.index(start_pos)] = end_pos
                        
                    else:
                        print(figure_horse)
                        white_or_black()
                        # figure_horse[figure_horse.index(start_pos)] = end_pos
                else:
                    print("white non correct path")
                    
                    first_hod = "black" if first_hod == "white" else "black"
                    first_hod = "white" if first_hod == "black" else "white"
        if correct_move:
            white_or_black()
        else:
            print("nice hod")
        
        figure_rook = figure["rook"]
        if start_pos in figure_rook:
            if first_hod == "black":
                
                if end_pos == (7, 4) and (7, 7) in figure_rook:
                    # короткая рокировка для белых
                    if (7, 5) not in white_pieces.values() and (7, 6) not in white_pieces.values():
                        if (7, 5) not in black_pieces.values() and (7, 6) not in black_pieces.values():
                            figure["king"][figure["king"].index((7, 4))] = (7, 6)
                            figure["rook"][figure["rook"].index((7, 7))] = (7, 5)
                # elif end_pos == (7, 2) and (7, 0) in figure_rook:  # длинная рокировка для белых
                    
                #     if (7, 3) not in white_pieces.values() and (7, 2) not in white_pieces.values() and (7, 1) not in white_pieces.values():
                #         if (7, 3) not in black_pieces.values() and (7, 2) not in black_pieces.values():
                #             print((7,2), (7,3))
                #             figure["king"][figure["king"].index((7, 4))] = (7, 2)
                #             figure["rook"][figure["rook"].index((7, 0))] = (7, 4)
                # if end_pos == (0, 6) and (0, 7) in figure_rook:  # короткая рокировка для черных
                #     print("black")
                #     if (0, 5) not in black_pieces.values() and (0, 6) not in black_pieces.values():
                #         if (0, 5) not in white_pieces.values() and (0, 6) not in white_pieces.values():
                #             figure["king"][figure["king"].index((0, 4))] = (0, 6)
                #             figure["rook"][figure["rook"].index((0, 7))] = (0, 5)
                # elif end_pos == (0, 2) and (0, 0) in figure_rook:  # длинная рокировка для черных
                #     print("black2")
                #     if (0, 3) not in black_pieces.values() and (0, 2) not in black_pieces.values() and (0, 1) not in black_pieces.values():
                #         if (0, 3) not in white_pieces.values() and (0, 2) not in white_pieces.values():
                #             figure["king"][figure["king"].index((0, 4))] = (0, 2)
                #             figure["rook"][figure["rook"].index((0, 0))] = (0, 3)
                else:
                    if end_pos[0] == start_pos[0] or end_pos[1] == start_pos[1]:
                        if end_pos not in black_pieces.values():
                            all_pieces = compare_list()


                            if end_pos in all_pieces:
                                for enemy_piece_type in enemy_pieces:
                                    if end_pos in enemy_pieces[enemy_piece_type]:
                                        figure_rook[figure_rook.index(start_pos)] = end_pos
                                        enemy_pieces[enemy_piece_type].remove(end_pos)
                                        break
                                else:
                                    print("no")
                            else:
                                figure_rook[figure_rook.index(start_pos)] = end_pos
                                print("Путь блокирован другой фигурой")
                        else:
                            print("Конечная позиция занята фигурой того же цвета")
            else:
                if end_pos == (0, 4) and (0, 7) in figure_rook:  # короткая рокировка для черных
                    print("black")
                    if (0, 5) not in black_pieces.values() and (0, 6) not in black_pieces.values():
                        if (0, 5) not in white_pieces.values() and (0, 6) not in white_pieces.values():
                            figure["king"][figure["king"].index((0, 4))] = (0, 6)
                            figure["rook"][figure["rook"].index((0, 7))] = (0, 5)
                # elif end_pos == (0, 2) and (0, 0) in figure_rook:  # длинная рокировка для черных
                #     print("black2")
                #     if (0, 3) not in black_pieces.values() and (0, 2) not in black_pieces.values() and (0, 1) not in black_pieces.values():
                #         if (0, 3) not in white_pieces.values() and (0, 2) not in white_pieces.values():
                            
                #             figure["king"][figure["king"].index((0, 4))] = (0, 2)
                #             figure["rook"][figure["rook"].index((0, 0))] = (0, 4)
                # if end_pos == (7, 6) and (7, 7) in figure_rook:
                #     print("white")  # короткая рокировка для белых
                #     if (7, 5) not in white_pieces.values() and (7, 6) not in white_pieces.values():
                #         if (7, 5) not in black_pieces.values() and (7, 6) not in black_pieces.values():
                #             figure["king"][figure["king"].index((7, 4))] = (7, 6)
                #             figure["rook"][figure["rook"].index((7, 7))] = (7, 5)
                # elif end_pos == (7, 2) and (7, 0) in figure_rook:  # длинная рокировка для белых
                #     print("white2")
                #     if (7, 3) not in white_pieces.values() and (7, 2) not in white_pieces.values() and (7, 1) not in white_pieces.values():
                #         if (7, 3) not in black_pieces.values() and (7, 2) not in black_pieces.values():
                #             figure["king"][figure["king"].index((7, 4))] = (7, 2)
                #             figure["rook"][figure["rook"].index((7, 0))] = (7, 3)
                else:
                    if end_pos[0] == start_pos[0] or end_pos[1] == start_pos[1]:
                        if end_pos not in white_pieces.values():
                            all_pieces = compare_list()
                            

                            if end_pos in all_pieces:
                                for enemy_piece_type in enemy_pieces:
                                    if end_pos in enemy_pieces[enemy_piece_type]:
                                        figure_rook[figure_rook.index(start_pos)] = end_pos
                                        enemy_pieces[enemy_piece_type].remove(end_pos)
                                        break
                                else:
                                    print("no")
                            else:
                                figure_rook[figure_rook.index(start_pos)] = end_pos
                                print("Путь блокирован другой фигурой")
                        else:
                            print("Конечная позиция занята фигурой того же цвета")

        figure_bishop = figure["bishop"]

        if start_pos in figure_bishop:
            if first_hod == "black":

                if abs(end_pos[0] - start_pos[0]) == abs(end_pos[1] - start_pos[1]):
                    if end_pos not in black_pieces.values():
                        all_pieces = compare_list()

                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    # Если да, то совершаем удар и удаляем фигуру противоположного цвета
                                    # white_or_black()
                                    figure_bishop[figure_bishop.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    break
                        
                                else:
                                    # white_or_black()
                                    print("no")
                        else:

                    
                            figure_bishop[figure_bishop.index(start_pos)] = end_pos
                    
                else:
                    pass

            else:
                if abs(end_pos[0] - start_pos[0]) == abs(end_pos[1] - start_pos[1]):
                    if end_pos not in white_pieces.values():
                        all_pieces = compare_list()
                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    figure_bishop[figure_bishop.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    break
                                    
                                else: pass
                        
                        else:
                            figure_bishop[figure_bishop.index(start_pos)] = end_pos

        figure_queen = figure["queen"]
        if start_pos in figure_queen:
            if first_hod == "black":
                if abs(end_pos[0]-start_pos[0]) == abs(end_pos[1]-start_pos[1])or\
                    (end_pos[0] == start_pos[0] or end_pos[1] == start_pos[1]):
                    if end_pos not in black_pieces.values():
                        all_pieces = compare_list()

                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:

                                    figure_queen[figure_queen.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    break
                                else:
                                    pass

                        else:
                            figure_queen[figure_queen.index(start_pos)] = end_pos
                        
            else:
                if abs(end_pos[0]-start_pos[0]) == abs(end_pos[1]-start_pos[1])or\
                    (end_pos[0] == start_pos[0] or end_pos[1] == start_pos[1]):
                    if end_pos not in black_pieces.values():
                        all_pieces = compare_list()
                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:

                                    figure_queen[figure_queen.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                else:
                                    pass
                        
                        else:
                            figure_queen[figure_queen.index(start_pos)] = end_pos
                else:
                    pass
        
        figure_king = figure["king"]

        if start_pos in figure_king:
            if first_hod == "black":
                print(end_pos, (start_pos[0]-1, start_pos[1]))
                if (end_pos == (start_pos[0]-1, start_pos[1]) or end_pos == (start_pos[0]-1, start_pos[1]-1) or\
                     (end_pos == (start_pos[0]-1, start_pos[1]+1) or end_pos == (start_pos[0]+1, start_pos[1])) or\
                        end_pos == (start_pos[0], start_pos[1]-1) or end_pos == (start_pos[0], start_pos[1]+1) or \
                            end_pos == (start_pos[0]+1, start_pos[1]-1) or end_pos == (start_pos[0]+1, start_pos[1]+1)):
                    print("black")
                    if end_pos not in black_pieces.values():
                        all_pieces = compare_list()

                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:

                                    figure_king[figure_king.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                else:
                                    pass
                        else:
                            figure_king[figure_king.index(start_pos)] = end_pos

            else:
                if abs(end_pos[0] - start_pos[0]) <= 1 and abs(end_pos[1] - start_pos[1]) <= 1:
                    print("white")
                    if end_pos not in black_pieces.values():
                        all_pieces = compare_list()
                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    
                                    figure_king[figure_king.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)

                                else: pass
                            
                        else:
                            figure_king[figure_king.index(start_pos)] = end_pos
                else: pass
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

lis = ["start", "START", "Start", "начать", "старт"]

def show_setting_page():
    screen.fill((255, 100, 50))
    draw_text("Settings", pygame.font.Font(None, 48), (0, 0, 0), screen, 600//2, 600//3)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Ожидание аудио-команды
        something = record_audio_and_recognize()
        print(something)
        if something == "before":
            show_start_page()
            waiting = False
def show_start_page():
    screen.fill((255, 255, 255))
    draw_text("Press Space to Start", pygame.font.Font(None, 48), (0, 0, 0), screen, 600//2, 600//3)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Если была нажата пробел, запускаем игру
                waiting = False
                time.sleep(1)
                # voise("игра началась, удачи")
                
                
    

# Первоначально показываем страницу "Start"
show_start_page()

current_skin = 1
def change_skin():
    global current_skin
    current_skin = 2 if current_skin ==1 else 1


def draw_poeces():
    if current_skin ==1:
        draw_pieces1()

    else:
        draw_pieces2()
previous_moves = [(0, 0)]
if "start" in lis:
    # show_start_page()
    selected = False
    run_game = True
    button = False
    while run_game:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run_game = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                button = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                
                if not selected:
                    # mouse_pos = pygame.mouse.get_pos()
                    try:
                        
                        start = record_audio_and_recognize()
                        print(start)
                        f = [f"fancy",f'fancy {start[-1]}', f"iphone {start[-1]}", f"definitely", f"infantry", f"avento", f"evan to"]
                        h = [f"age and {start[-1]}", f"agent {start[-1]}", f"asian {start[-1]}", f'age {start[-1]}', f"regent {start[-1]}", f"agency"]
                        a = [f"i am too", f"i am {start[-1]}", f"i am to", f'a.m. to']
                        c = [f"siento", f"cnc", f'cm to']
                        g = [f"gmc"]
                        if start.lower() in h:
                            
                            start = f"h{start[-1]}"
                        elif start.lower() in f:
                            
                            start = f"f{start[-1]}"
                        index1, index2 = start[0].lower(), start[-1]
                        row1=ord(index1)-97
                        col1=int(index2)-1
                        start_pos = (row1, col1)
                        if sqSelected == (row1, col1):
                            sqSelected = ()
                            PlayerClick = []
                        else:
                            sqSelected = (row1, col1)
                            PlayerClick.append(sqSelected)
                            
                            
                            selected = True
                    except ValueError or ConnectionResetError:
                        print("некоректний ввід")
                        continue
                    # mcol = mouse_pos[0] // sq_size
                    # mrow = mouse_pos[1] // sq_size
                    
                else:
                    
                    try:
                        
                        end = record_audio_and_recognize()
                        print(end)
                        e_f = [f'fancy {end[-1]}', f"iphone {end[-1]}"]
                        if end.lower() in e_f:
                            end = f"f{end[-1]}"
                        
                        index3, index4 = end[0].lower(), end[-1]

                        print(end)
                        row=ord(index3)-97
                        col=int(index4)-1
                        # end_pos = pygame.mouse.get_pos()
                        end_pos = (row, col)
                        print(end_pos)
                        print(sqSelected)
                        
                        if start_pos != end_pos:
                            white_or_black()
                            move_chess(sqSelected, end_pos)
                        selected = False  
                        previous_moves.append(((index1, index2), (index3, index4)))
                    except ValueError or ConnectionResetError:
                        print("некоректний ввід")
                        continue
                    # if mouse_pos != end_pos:
                    #     white_or_black()
                    #     move_chess(sqSelected, end_pos)
                    # selected = False  
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                print("hello")
                white_or_black()

        for move in previous_moves:
            start, end = move

        screen.fill((255,255,255))
        draw_board(sqSelected)
        
        draw_button()
        # screen.fill((0,0,0))
        text1 = "prewiev hod"
        text2 = f"{start} : {end}"
        draw_pieces1()
        if button:
            
            draw_board(sqSelected)
            draw_pieces2()
            
            # button = False
        

        
        prviews_hod = pygame.font.Font(None, 24)
        hod1 = prviews_hod.render(text1, True, (0,0,0))
        hod2 = prviews_hod.render(text2, True, (0,0,0))
        text_hod1 = hod1.get_rect(center = (800-100, 100))
        text_hod2 = hod2.get_rect(center = (800-100, 120))
        screen.blit(hod1, text_hod1)
        screen.blit(hod2, text_hod2)
        
        font = pygame.font.Font(None, 40)

        text = font.render(f"turn: {first_hod}", True, (0, 0, 0))
        text_rect = text.get_rect(center=(800-100, 50))
        

        screen.blit(text, text_rect)
       
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

else:
    print("i dont understand you")