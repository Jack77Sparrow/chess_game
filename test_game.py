import pygame
import sys
from figure import record_audio_and_recognize
# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Определение размеров доски
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = HEIGHT // 8

class ChessBoard:
    def __init__(self):
        self.board = [["." for _ in range(8)] for _ in range(8)]

    def draw(self, screen):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else GRAY
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, screen):
        pass  # Здесь можно будет добавить отображение фигур

class Player:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.x = col * SQUARE_SIZE
        self.y = row * SQUARE_SIZE
        self.width = SQUARE_SIZE
        self.height = SQUARE_SIZE
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_to(self, row, col):
        self.row = row
        self.col = col
        self.x = col * SQUARE_SIZE
        self.y = row * SQUARE_SIZE

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Создание объекта шахматной доски
chess_board = ChessBoard()

# Создание игрока-кубика
player1 = Player(0, 0, RED)
player2 = Player(7, 7, GREEN)
# Основной игровой цикл
current_player = player1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ввод координат из терминала
    # row, col = record_audio_and_recognize()
    try:
        text = record_audio_and_recognize()
        index1, index2 = text[0].lower(), text[-1]
        
        row=ord(index1)-97
        col=int(index2)-1
        
        current_player.move_to(row, col)
        current_player = player1 if current_player == player2 else player2
    except ValueError:
        print("Некорректный ввод!")

    screen.fill(BLACK)
    chess_board.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
