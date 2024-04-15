from chess import sq_size, size
import pygame
def images():
    black_pawn = pygame.image.load('photos/black/pawn.png')
    chess_rect = black_pawn.get_rect()
    black_pawn = pygame.transform.scale(black_pawn, (size, size))


    #біла пешка
    white_pawn = pygame.image.load('photos/white/pawn (1).png')
    white_pawn_rect = white_pawn.get_rect()
    white_pawn = pygame.transform.scale(white_pawn, (size, size))


    #чорний кінь
    black_horse = pygame.image.load("photos/black/black_horse.png")
    black_horse_rect = black_horse.get_rect()
    black_horse = pygame.transform.scale(black_horse, (size, size))


    white_horse = pygame.image.load('photos/white/horse.png')
    white_horse_rect = white_horse.get_rect()
    white_horse = pygame.transform.scale(white_horse, (size, size))


    black_rook = pygame.image.load('photos/black/rook.png')
    black_rook_rect = black_rook.get_rect()
    black_rook = pygame.transform.scale(black_rook, (size, size))

    white_rook = pygame.image.load('photos/white/rook.png')
    white_rook_rect = white_rook.get_rect()
    white_rook = pygame.transform.scale(white_rook, (size, size))

    black_bishop = pygame.image.load('photos/black/bishop.png')
    black_bishop_rect = black_bishop.get_rect()
    black_bishop = pygame.transform.scale(black_bishop, (size, size))

    white_bishop = pygame.image.load('photos/white/bishop.png')
    white_bishop_rect = white_bishop.get_rect()
    white_bishop = pygame.transform.scale(white_bishop, (size, size))


    black_king = pygame.image.load('photos/black/king.png')
    black_king_rect = black_king.get_rect()
    black_king = pygame.transform.scale(black_king, (size, size))

    white_king = pygame.image.load('photos/white/king.png')
    white_king_rect = white_king.get_rect()
    white_king = pygame.transform.scale(white_king, (size, size))


    black_queen = pygame.image.load('photos/black/queen.png')
    black_queen_rect = black_queen.get_rect()
    black_queen = pygame.transform.scale(black_queen, (size, size))

    white_queen = pygame.image.load('photos/white/queen.png')
    white_queen_rect = white_queen.get_rect()
    white_queen = pygame.transform.scale(white_queen, (size, size))