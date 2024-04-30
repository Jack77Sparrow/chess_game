import pygame
import sys
import os

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движущиеся спрайты")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений для анимации
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            images.append(pygame.image.load(path))
    return images

image_folder = '/Users/drake/Desktop/vscode/oshi/progect/photos/sprites'

# Загрузка изображений для анимации
player_images = load_images_from_folder(image_folder)

# Класс для спрайта персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_index = 0
        self.image = player_images[self.image_index]
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.speed = 1

    def update(self):
        # Анимация движения: переключение изображений
        self.image_index = (self.image_index + 1) % len(player_images)
        self.image = player_images[self.image_index]
        
        # Движение персонажа по горизонтали
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        # Обработка выхода за границы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Создание группы спрайтов и добавление персонажа в нее
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Функция для отрисовки текста на экране
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Функция для отображения начального экрана
def show_start_screen():
    screen.fill(BLACK)
    draw_text("Нажмите Пробел, чтобы начать", pygame.font.Font(None, 48), WHITE, screen, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Основной игровой цикл
running = True
show_start_screen()
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Переход к игре при нажатии на пробел
            show_start_screen()

    # Обновление экрана
    screen.fill(WHITE)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
