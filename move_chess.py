import pygame


first_hod = 'black'
def white_or_black():
    global first_hod
    first_hod = "white" if first_hod == "black" else 'black'

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


class Pawn():
    def __init__(self, color):
        self.color = color
        
    def move(self, start_pos, end_pos, enemy_pieces, figure_type):
        if self.color == "black":
            if start_pos[0] == 6 and end_pos == (start_pos[0]-2, start_pos[1]) or end_pos == (start_pos[0]-1, start_pos[1]):
                    
                    
                all_pieces = compare_list()

                if end_pos in all_pieces:
                    pass
                    # white_or_black()
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
                    # white_or_black()
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
            
        white_or_black() 

       
            
