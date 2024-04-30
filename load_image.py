import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра")

# Задание цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Загрузка фонового изображения
background = pygame.image.load("/Users/drake/Desktop/vscode/oshi/progect/1620071300_10-pibig_info-p-anime-tyanki-na-chernom-fone-anime-krasivo-10.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Функция для отрисовки текста на экране
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Главная функция начального экрана
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Переход к основной части игры
                    # Здесь вызывайте вашу основную игровую функцию
                    return

        # Отрисовка фона и текста на экране
        screen.blit(background, (0, 0))
        draw_text("Нажмите Пробел, чтобы начать", pygame.font.Font(None, 48), WHITE, screen, screen_width // 2, screen_height // 2)
        draw_text("Нажмите Esc, чтобы выйти", pygame.font.Font(None, 36), WHITE, screen, screen_width // 2, screen_height // 1.5)

        pygame.display.flip()

# Запуск начального экрана
main_menu()
