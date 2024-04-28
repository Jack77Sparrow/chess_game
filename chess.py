import pygame
import sys
import os
from const import *
from figure import record_audio_and_recognize

pygame.init()

pygame.display.set_caption("Chess game")


#initialised a values
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
            if i == 0:
                font = pygame.font.Font(None, 36)
                text_surface = font.render(chr(97 + j), True, black)  # Використання chr(97 + j) для отримання a, b, c
                screen.blit(text_surface, (j * sq_size + 10, i * sq_size + 10))
            # Додати позначення для рядків (1, 2, 3)
            if j == 0:
                font = pygame.font.Font(None, 36)
                text_surface = font.render(str(i + 1), True, black)  # Використання str(i + 1) для отримання 1, 2, 3
                screen.blit(text_surface, (j * sq_size + 10, i * sq_size + 10))


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
                        
                        all_pieces = compare_list()
                        if end_pos in all_pieces:
                            # await asyncio.sleep(0.5)
                            
                            for enemy_piece_type in enemy_pieces:

                                if end_pos in enemy_pieces[enemy_piece_type]:
                                    # white_or_black()
                                    
                                    
                                    figure_horse[figure_horse.index(start_pos)] = end_pos
                                    enemy_pieces[enemy_piece_type].remove(end_pos)
                                    break
                                
                                else:
                                    
                                    print(1)

                                
                        else:
                            # white_or_black()
                            figure_horse[figure_horse.index(start_pos)] = end_pos
                    else:
                        
                        white_or_black()
                        # figure_horse[figure_horse.index(start_pos)] = end_pos
                else:
                    print("non correct path")
            else:
                
                if (end_pos == (start_pos[0]-2, start_pos[1]-1) or end_pos == (start_pos[0]-2, start_pos[1]+1) or 
                    end_pos == (start_pos[0]+2, start_pos[1]-1) or end_pos == (start_pos[0]+2, start_pos[1]+1) or
                    end_pos == (start_pos[0]-1, start_pos[1]+2) or end_pos == (start_pos[0]+1, start_pos[1]+2) or
                    end_pos == (start_pos[0]-1, start_pos[1]-2) or end_pos == (start_pos[0]+1, start_pos[1]-2)):
                    
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
                else:
                    print("non correct path")
        
        
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

lis = ["start", "START", "Start", "начать", "старт"]

if "start" in lis:
    selected = False
    run_game = True
    while run_game:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not selected:
                    # mouse_pos = pygame.mouse.get_pos()
                    try:
                        
                        start = record_audio_and_recognize()
                            
                        
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
                    except ValueError:
                        print("некоректний ввід")
                    # mcol = mouse_pos[0] // sq_size
                    # mrow = mouse_pos[1] // sq_size
                    
                else:

                    try:
                        try:
                            end = record_audio_and_recognize()
                        except ConnectionResetError:
                            
                            continue
                        index1, index2 = end[0].lower(), end[-1]
                        print(end)
                        row=ord(index1)-97
                        col=int(index2)-1
                        # end_pos = pygame.mouse.get_pos()
                        end_pos = (row, col)
                        print(end_pos)
                        print(sqSelected)
                        if start_pos != end_pos:
                            white_or_black()
                            move_chess(sqSelected, end_pos)
                        selected = False  
                    except ValueError:
                        print("Некорректный ввод!")
                    # if mouse_pos != end_pos:
                    #     white_or_black()
                    #     move_chess(sqSelected, end_pos)
                    # selected = False  
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

else:
    print("i dont understand you")