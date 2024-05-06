import pygame


Dimensions = 8
whidth = 600
height = 600
sq_size = whidth // 8
size = sq_size // 1.3
screen = pygame.display.set_mode((800, height))
white = pygame.Color(225, 225, 225)
black = pygame.Color(0, 0, 0)
grey = pygame.Color(150, 75, 0)

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
