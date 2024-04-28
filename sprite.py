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
WHITE = (0, 0, 0)

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

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    screen.fill(WHITE)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.Clock().tick(17)

pygame.quit()
sys.exit()
