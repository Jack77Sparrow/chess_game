import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
WHITE = (255, 255, 255)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)
def show_start_page():
    screen.fill(WHITE)
    draw_text("putt space", pygame.font.Font(None, 48), (0, 0, 0), screen, 600//2, 600//2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
    return
        


