import pygame
from menu import Menu  

class Nave:
    """
    Classe que representa a nave.
    A nave atualiza sua posição, lida com colisões e é desenhada na tela.
    """
    def __init__(self, window, width=None, height=None):
        """
        Inicializa a nave.
        pygame.Surface: A superfície da janela do jogo.
        width: Largura da imagem da nave.
        height: Altura da imagem da nave.
        """
        self.window = window
        self.images = {
            'up': pygame.image.load('imagens/nave.png'),
            'down': pygame.image.load('imagens/nave_caindo.png'),
        }
        
        if width and height:
            self.images['up'] = pygame.transform.scale(self.images['up'], (width, height))
            self.images['down'] = pygame.transform.scale(self.images['down'], (width, height))

        self.image = self.images['down']  
        self.mask = pygame.mask.from_surface(self.image)
        self.initial_x = 400  
        self.initial_y = 100
        self.x = 400  
        self.y = 100  
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))  
        
        self.velocity = 0  
        self.gravity = 0.6  
        self.flap_strength = -9  
        self.visible = True 

    def update(self, obstacles):
        """
        Atualiza a posição da nave e lida com colisões com obstáculos.
        obstacles: Objeto que contém a lista de obstáculos.
        Retorna:
            True se uma colisão foi detectada, False caso contrário.
        """
        tempo_inicio = pygame.time.get_ticks()
        self.velocity += self.gravity
        self.y += self.velocity

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
        self.hitbox.y = self.y  
        
        for obstacle in obstacles.obstacles:
            offset_x = obstacle['x'] - self.x
            offset_y = obstacle['y'] - self.y
            if self.mask.overlap(obstacle['mask'], (offset_x, offset_y)):
                self.visible = False
                return True  
        return False  
  
    def draw(self):
        """
        Desenha a nave na tela.
        """
        if self.visible:
            self.window.blit(self.image, (self.x, self.y))
        