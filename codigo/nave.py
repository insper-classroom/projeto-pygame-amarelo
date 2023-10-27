import pygame
from menu import Menu  # Importe a classe Menu

class Nave:
    def __init__(self, window, width=None, height=None):  # Adicione parâmetros de largura e altura
        self.window = window
        self.images = {
            'up': pygame.image.load('imagens/nave.png'),
            'down': pygame.image.load('imagens/nave_caindo.png')
        }
        # Se width e height forem especificados, redimensiona a imagem
        if width and height:
            self.images['up'] = pygame.transform.scale(self.images['up'], (width, height))
            self.images['down'] = pygame.transform.scale(self.images['down'], (width, height))

        self.image = self.images['down']  # Imagem inicial
        self.mask = pygame.mask.from_surface(self.image)
        self.x = 400  # Posição inicial x
        self.y = 100  # Posição inicial y
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))  # Criar o hitbox
        
        self.velocity = 0  # Velocidade vertical inicial
        self.gravity = 0.6  # Força da gravidade
        self.flap_strength = -9  # Força do impulso para cima

    def update(self, obstacles):  # Passar os obstáculos como argumento]
        self.velocity += self.gravity
        self.y += self.velocity

        # Alternanr as imagens caso subindo ou descendo.
        if self.velocity < 0:
            self.image = self.images['up']
        else:
            self.image = self.images['down']
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.hitbox.top > 0:
            self.y -= 5
        if keys[pygame.K_DOWN] and self.hitbox.bottom < 1080:
            self.y += 5
        if keys[pygame.K_SPACE] and self.hitbox.top > 0:         
            self.velocity = self.flap_strength
        self.hitbox.y = self.y  # Atualizar a posição y do hitbox
        
        # Verificar colisões com obstáculos

        for obstacle in obstacles.obstacles:
            offset_x = obstacle['x'] - self.x
            offset_y = obstacle['y'] - self.y
            if self.mask.overlap(obstacle['mask'], (offset_x, offset_y)):
                return True  # Colisão detectada
        return False  # Nenhuma colisão detectada
    def draw(self): 
        self.window.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(self.window, (255, 0, 0), self.hitbox, 2)