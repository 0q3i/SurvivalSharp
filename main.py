import pygame
import sys
from win32api import GetSystemMetrics

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Taille de la fenêtre
WIDTH, HEIGHT = GetSystemMetrics(0) * 0.95, GetSystemMetrics(1) * 0.95

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Sharp")

# Police de texte
font = pygame.font.Font(None, 32)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def login():
    running = True
    username = ""
    password = ""
    login_txt = font.render("Login", 1, WHITE)
    background = pygame.image.load("./assets/background.png")

    while running:
        screen.blit(background, (0,0))
        s = pygame.Surface((WIDTH*0.2,HEIGHT))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill(BLACK)           # this fills the entire surface
        screen.blit(s, (0,0))    # (0,0) are the top-left coordinates

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    login()
