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
#new comment
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


sqSelected = ()
PlayerClick = []
def move_chess(event):
    global white_pieces,first_hod, black_pieces
    row, col = event
    sq_row = row // sq_size
    sq_col = col // sq_size
    new_pos = (sq_col, sq_row)
    # Update the position of the 
    sqSelected = (sq_col, sq_row)
    print(sq_row)
    print(sqSelected)
    
    if first_hod == "white":
        figure = white_pieces
        enemy_pieces = black_pieces
        

    else:
        figure = black_pieces
        enemy_pieces = white_pieces
    print(figure['pawn'])
    # print(sqSelected)
    if sqSelected in figure['pawn']:
        print('yes')
        if new_pos == (4, 0):


            white_pieces['pawn'][0] = new_pos  # Assuming you're updating the first pawn
        else:
            pass
            
    





run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # move_chess(mouse_pos)
            white_or_black()
            col = mouse_pos[0] // sq_size
            row = mouse_pos[1]//sq_size
            if sqSelected == (row, col):
                sqSelected = ()
                PlayerClick = []
            else:

                sqSelected = (row, col)
                PlayerClick.append(sqSelected)
            if len(PlayerClick) == 2:
                pass
            move_chess(mouse_pos)


    draw_board()
    draw_pieces()
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
sosi
