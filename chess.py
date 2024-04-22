import pygame
import sys
import os
from const import *


pygame.init()

pygame.display.set_caption("Chess game")


red = pygame.Color(255, 0, 0)

    

images = {}
for color in colors:
    for piece in pieces:
        img_path = os.path.join(image_folder, color, f"{color}_{piece}.png")
        img = pygame.transform.scale(pygame.image.load(img_path), (size, size))
        images[f"{color}_{piece}"] = img



def draw_board(selected_sq):
    for i in range(Dimensions):
        for j in range(0, Dimensions):
            if (i + j) % 2 == 0:
                color = white
            else:
                color = grey
            if (i, j) == selected_sq:
                color = red
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


class InvalidMoveError(Exception):
    pass


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
    global text, text_rect
    global lists_of_black, lists_of_white
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
                

                if start_pos[0] == 6 and end_pos == (start_pos[0]-2, start_pos[1]) or end_pos == (start_pos[0]-1, start_pos[1]):
                    
                    lists_of_black = []
                    for b_value in black_pieces.values():
                        for v in b_value:
                            lists_of_black.append(v)
                    # print(black_pieces)
                    lists_of_white = []
                    for w_value in white_pieces.values():
                        for w in w_value:
                            lists_of_white.append(w)
                    # print(lists_of_black)
                    if end_pos in lists_of_black + lists_of_white:
                        white_or_black()
                        # print("yes")
                        
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
                    lists_of_white = []
                    for w_value in white_pieces.values():
                        for w in w_value:
                            lists_of_white.append(w)
                    lists_of_black = []
                    for b_value in black_pieces.values():
                        for v in b_value:
                            lists_of_black.append(v)
                    # print(lists_of_white)
                    
                    if end_pos in lists_of_white + lists_of_black:
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

        figure_horse = figure["horse"]

        if start_pos in figure_horse:

            if first_hod == "black":

                if (end_pos == (start_pos[0]-2, start_pos[1]-1) or end_pos == (start_pos[0]-2, start_pos[1]+1) or 
                    end_pos == (start_pos[0]+2, start_pos[1]-1) or end_pos == (start_pos[0]+2, start_pos[1]+1) or
                    end_pos == (start_pos[0]-1, start_pos[1]+2) or end_pos == (start_pos[0]+1, start_pos[1]+2) or
                    end_pos == (start_pos[0]-1, start_pos[1]-2) or end_pos == (start_pos[0]+1, start_pos[1]-2)):
                    # print(end_pos)
                    # print("___")
                    # print((start_pos[0]-2, start_pos[1]-1))
                    # print("---")
                    # print(figure_horse)
                    
                    if end_pos not in black_pieces.values():
                        
                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)
                        if end_pos in lists_of_black+lists_of_white:
                            # await asyncio.sleep(0.5)
                            
                            for enemy_piece_type in enemy_pieces:

                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    # white_or_black()
                                    
                                    
                                    figure_horse[figure_horse.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    break
                                
                                else:
                                    
                                    print(1)
                            # white_or_black()
                                    
                                    # white_or_black()

                                    # figure_horse[figure_horse.index(start_pos)] = start_pos


                                
                        else:
                            # white_or_black()
                            figure_horse[figure_horse.index(start_pos)] = end_pos
                    else:
                        
                        white_or_black()
                        # figure_horse[figure_horse.index(start_pos)] = end_pos
                else:
                    pass
            else:
                
                if (end_pos == (start_pos[0]-2, start_pos[1]-1) or end_pos == (start_pos[0]-2, start_pos[1]+1) or 
                    end_pos == (start_pos[0]+2, start_pos[1]-1) or end_pos == (start_pos[0]+2, start_pos[1]+1) or
                    end_pos == (start_pos[0]-1, start_pos[1]+2) or end_pos == (start_pos[0]+1, start_pos[1]+2) or
                    end_pos == (start_pos[0]-1, start_pos[1]-2) or end_pos == (start_pos[0]+1, start_pos[1]-2)):
                    
                    if end_pos not in white_pieces.values():
                        
                        

                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)
                        # white_or_black()
                        if end_pos in lists_of_white + lists_of_black:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    # Если да, то совершаем удар и удаляем фигуру противоположного цвета
                                    # white_or_black()
                                    figure_horse[figure_horse.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    break
                            
                                else:
                                    # white_or_black()
                                    print("no")
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
            
        
        # def is_path_clear(start_pos, end_pos, all_pieces):
        #     # Проверяем, движется ли ладья по горизонтали или вертикали
        #     if start_pos[0] == end_pos[0]:  # Проверяем вертикальное движение
        #         start_row, end_row = min(start_pos[1], end_pos[1]), max(start_pos[1], end_pos[1])
        #         for row in range(start_row + 1, end_row):
        #             if (start_pos[0], row) in all_pieces:
        #                 return False  # На пути есть фигура
        #     elif start_pos[1] == end_pos[1]:  # Проверяем горизонтальное движение
        #         start_col, end_col = min(start_pos[0], end_pos[0]), max(start_pos[0], end_pos[0])
        #         for col in range(start_col + 1, end_col):
        #             if (col, start_pos[1]) in all_pieces:
        #                 return False  # На пути есть фигура
        #     else:
        #         # Ладья движется не по вертикали и не по горизонтали, это недопустимый ход для ладьи
        #         return False
            
        #     return True  # Если препятствий нет на пути, возвращаем True
        figure_rook = figure["rook"]
        if start_pos in figure_rook:
            if first_hod == "black":
                
                if end_pos == (7, 4) and (7, 7) in figure_rook:
                    # короткая рокировка для белых
                    if (7, 5) not in white_pieces.values() and (7, 6) not in white_pieces.values():
                        if (7, 5) not in black_pieces.values() and (7, 6) not in black_pieces.values():
                            figure["king"][figure["king"].index((7, 4))] = (7, 7)
                            figure["rook"][figure["rook"].index((7, 7))] = (7, 4)
                elif end_pos == (7, 2) and (7, 0) in figure_rook:  # длинная рокировка для белых
                    
                    if (7, 3) not in white_pieces.values() and (7, 2) not in white_pieces.values() and (7, 1) not in white_pieces.values():
                        if (7, 3) not in black_pieces.values() and (7, 2) not in black_pieces.values():
                            print((7,2), (7,3))
                            figure["king"][figure["king"].index((7, 4))] = (7, 2)
                            figure["rook"][figure["rook"].index((7, 0))] = (7, 4)
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
                            lists_of_white = []
                            for w_value in white_pieces.values():
                                for w in w_value:
                                    lists_of_white.append(w)
                            lists_of_black = []
                            for b_value in black_pieces.values():
                                for v in b_value:
                                    lists_of_black.append(v)
                            all_pieces = lists_of_white + lists_of_black

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
                            figure["king"][figure["king"].index((0, 4))] = (0, 7)
                            figure["rook"][figure["rook"].index((0, 7))] = (0, 4)
                elif end_pos == (0, 2) and (0, 0) in figure_rook:  # длинная рокировка для черных
                    print("black2")
                    if (0, 3) not in black_pieces.values() and (0, 2) not in black_pieces.values() and (0, 1) not in black_pieces.values():
                        if (0, 3) not in white_pieces.values() and (0, 2) not in white_pieces.values():
                            
                            figure["king"][figure["king"].index((0, 4))] = (0, 2)
                            figure["rook"][figure["rook"].index((0, 0))] = (0, 4)
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
                            lists_of_white = []
                            for w_value in white_pieces.values():
                                for w in w_value:
                                    lists_of_white.append(w)
                            lists_of_black = []
                            for b_value in black_pieces.values():
                                for v in b_value:
                                    lists_of_black.append(v)
                            all_pieces = lists_of_white + lists_of_black

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
                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)
                        all_pieces = lists_of_black + lists_of_white
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
                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)

                        all_pieces = lists_of_black + lists_of_white
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
                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)

                        all_pieces = lists_of_black + lists_of_white

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
                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)

                        all_pieces = lists_of_black + lists_of_white
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
                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)

                        all_pieces = lists_of_black + lists_of_white

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
                        lists_of_white = []
                        for w_value in white_pieces.values():
                            for w in w_value:
                                lists_of_white.append(w)
                        lists_of_black = []
                        for b_value in black_pieces.values():
                            for v in b_value:
                                lists_of_black.append(v)

                        all_pieces = lists_of_black + lists_of_white
                        if end_pos in all_pieces:
                            for enemy_piece_type in enemy_pieces:
                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    
                                    figure_king[figure_king.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)

                                else: pass
                            
                        else:
                            figure_king[figure_king.index(start_pos)] = end_pos
                else: pass


selected = False
run_game = True
while run_game:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not selected:
                mouse_pos = pygame.mouse.get_pos()
                
                
                col = mouse_pos[0] // sq_size
                row = mouse_pos[1] // sq_size
                if sqSelected == (row, col):
                    sqSelected = ()
                    PlayerClick = []
                else:
                    sqSelected = (row, col)
                    PlayerClick.append(sqSelected)
                    selected = True
            else:


        
                end_pos = pygame.mouse.get_pos()
                if mouse_pos != end_pos:
                    white_or_black()
                    move_chess(sqSelected, end_pos)
                selected = False  
        elif event.type == pygame.K_DOWN:
            print("hello")
            white_or_black()

       

    screen.fill((255,255,255))
    draw_board(sqSelected)
    draw_pieces()
    # screen.fill((0,0,0))
    font = pygame.font.Font(None, 40)
    text = font.render(f"turn: {first_hod}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(800-100, 50))
    

    screen.blit(text, text_rect)
    pygame.display.flip()
    
pygame.quit()
sys.exit()
