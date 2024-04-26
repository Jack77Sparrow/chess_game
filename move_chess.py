import pygame
from chess import compare_list


print(compare_list())
# class Pawn():
#     def __init__(self, color):
#         self.color = color
        
#     def move(self, start_pos, end_pos, enemy_pieces):
#         if self.color == "black":
#             if start_pos[0] == 6 and end_pos == (start_pos[0]-2, start_pos[1]) or end_pos == (start_pos[0]-1, start_pos[1]):
                    
                    
#                 all_pieces = compare_list()

#                 if end_pos in all_pieces:
#                     white_or_black()
#                 else:
#                     figure_type[figure_type.index(start_pos)] = end_pos
                
#             elif end_pos == (start_pos[0] - 1, start_pos[1] - 1) or end_pos == (start_pos[0] - 1, start_pos[1] + 1):
                
#                 # print((start_pos[0] - 1, start_pos[1] - 1), (start_pos[0] - 1, start_pos[1] + 1))
#                 # Проверяем, находится ли на конечной позиции фигура противоположного цвета
#                 for enemy_piece_type in enemy_pieces:
#                     if end_pos in enemy_pieces[enemy_piece_type]:
#                         # Если да, то совершаем удар и удаляем фигуру противоположного цвета
#                         figure_type[figure_type.index(start_pos)] = end_pos
#                         enemy_pieces[enemy_piece_type].remove(end_pos)
#                         break
            
