import pygame
pygame.font.init()
font = pygame.font.Font(None, 36)
def display_text(screen, text, x, y):
    text = font.render(str(text), 1, (255, 255, 255))
    screen.blit(text, (x, y))