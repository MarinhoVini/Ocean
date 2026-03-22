import pygame
from code.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.levels = []

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Lógica do jogo aqui
            pygame.display.flip()
        pygame.quit()
