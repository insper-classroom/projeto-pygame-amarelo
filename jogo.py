



import pygame
import math
import random

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Flap Bird')
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Atualizar objetos do jogo aqui
            # ...

            # Desenhar objetos do jogo aqui
            # ...

            pygame.display.flip()

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Adicione mais atributos conforme necessário

    def update(self):
        # Atualize a posição e outros atributos do pássaro aqui
        pass

    def draw(self, window):
        # Desenhe o pássaro na janela aqui
        pass

class Obstacle:
    def __init__(self, x, width, gap_height):
        self.x = x
        self.width = width
        self.gap_height = gap_height
        # Adicione mais atributos conforme necessário

    def update(self):
        # Atualize a posição e outros atributos do obstáculo aqui
        pass

    def draw(self, window):
        # Desenhe o obstáculo na janela aqui
        pass

# Inicializando e rodando o jogo
game = Game()
game.run()



