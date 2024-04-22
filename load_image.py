import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 480, 480

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размеры клетки
CELL_SIZE = WIDTH // 8

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Шахматная доска')

# Отрисовка шахматной доски
def draw_board():
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Отрисовка персонажа
def draw_character(color, x, y):
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Основной игровой цикл
def main():
    red_character_pos = (0, 0)    # Начальные координаты красного персонажа
    green_character_pos = (7, 7)  # Начальные координаты зеленого персонажа
    selected = False              # Персонаж выбран или нет

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not selected:
                    # Если персонаж не выбран, выбираем его
                    x, y = pygame.mouse.get_pos()
                    if red_character_pos == (x // CELL_SIZE, y // CELL_SIZE):
                        selected = True
                        selected_color = RED
                    elif green_character_pos == (x // CELL_SIZE, y // CELL_SIZE):
                        selected = True
                        selected_color = GREEN
                else:
                    # Если персонаж уже выбран, перемещаем его
                    x, y = pygame.mouse.get_pos()
                    new_pos = x // CELL_SIZE, y // CELL_SIZE
                    if selected_color == RED:
                        red_character_pos = new_pos
                    elif selected_color == GREEN:
                        green_character_pos = new_pos
                    selected = False

        screen.fill(GRAY)
        draw_board()
        draw_character(RED, *red_character_pos)
        draw_character(GREEN, *green_character_pos)
        pygame.display.flip()

if __name__ == '__main__':
    main()
