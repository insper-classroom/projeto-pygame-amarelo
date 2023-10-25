import pygame
import math
import random
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('Star Adventure')
        self.fundo = pygame.image.load('imagens/fundo_planeta.png')
        self.fundo = pygame.transform.scale(self.fundo, (1600, 860))
        
        self.running = True
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.running = False
            collision_detected = nave.update(obstacles)
            if collision_detected:
                game.running = False
            # Atualizar objetos do jogo aqui
            # ...
            self.window.blit(self.fundo, (180, 110))
            obstacles.update()
            obstacles.draw()
            nave.update(obstacles)
            nave.draw()
            # Desenhar objetos do jogo aqui
            # ...
            pygame.display.flip()
class Nave:
    def __init__(self, window, width=None, height=None):  # Adicione parâmetros de largura e altura
        self.window = window
        self.image = pygame.image.load('imagens/nave.png')  # Carregar a imagem da nave
        
        # Se width e height forem especificados, redimensiona a imagem
        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height))

        self.x = 400  # Posição inicial x
        self.y = 300  # Posição inicial y
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))  # Criar o hitbox
        # hitbox_width = self.image.get_width() * 0.7  # 70% da largura da imagem
        # hitbox_height = self.image.get_height() * 0.6  # 60% da altura da imagem
        # hitbox_x = self.x + self.image.get_width() * 0.10  # Centraliza o hitbox
        # hitbox_y = self.y + self.image.get_height() * 0.20  # Ajusta a posição vertical do hitbox

        # self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

    def update(self, obstacles):  # Passar os obstáculos como argumento
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.hitbox.top > 0:
            self.y -= 5
        if keys[pygame.K_DOWN] and self.hitbox.bottom < 1080:
            self.y += 5
        
        self.hitbox.y = self.y  # Atualizar a posição y do hitbox
        
        # Verificar colisões com obstáculos
        for obstacle in obstacles.obstacles:
            if self.hitbox.colliderect(obstacle['hitbox']):
                return True  # Retorna True se uma colisão for detectada
        return False
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(self.window, (255, 0, 0), self.hitbox, 2)
class Obstacle:
    def __init__(self, window):
        self.window = window
        self.obstacles = []
    def initialize_obstacle(self, obstacle_type, x, y, width=None, height=None):
        obstacles = {
            'platform': 'imagens/plataforma.png',
            'clif': 'imagens/obstaculo_chao.png',
            'nuddle': 'imagens/obstaculo_ceu.png'
        }
        image = pygame.image.load(obstacles[obstacle_type])
        # Apenas para redimensionar a imagem.
        if width and height: # Caso especificado a largura e altura na hora de iniciar o jogo.
            image = pygame.transform.scale(image, (width, height))

        hitbox = image.get_rect(topleft=(x, y))
        # if obstacle_type == 'clif':
        #     # Ajuste o hitbox aqui para o 'clif'
        #     hitbox_width = image.get_width() * 0.7  # Exemplo: 70% da largura da imagem
        #     hitbox_height = (image.get_height() * 0.7)   # Exemplo: 70% da altura da imagem
        #     hitbox_x = x + image.get_width() * 0.15  # Exemplo: Centraliza o hitbox
        #     hitbox_y = y + image.get_height() * 0.20  # Exemplo: Centraliza o hitbox
        #     hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)
        # else:
        #     hitbox_width = image.get_width() * 0.8  # 80% da largura da imagem
        #     hitbox_height = (image.get_height() * 0.8) + 10  # 80% da altura da imagem
        #     hitbox_x = x + image.get_width() * 0.1  # Centraliza o hitbox
        #     hitbox_y = y + image.get_height() * 0.1  # Centraliza o hitbox

        # hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

        obstacle_images = {
            'type': obstacle_type,
            'x': x,
            'y': y,
            'image': image,
            'hitbox': hitbox
        }
        self.obstacles.append(obstacle_images)
    def update(self):
        # Atualize a posição e outros atributos do obstáculo aqui
        for obstacle in self.obstacles:
            obstacle['x'] -= 5
            obstacle['hitbox'].x -= 5
            if obstacle['x'] + obstacle['hitbox'].width < 0:
                if obstacle['type'] == 'platform':
                    obstacle['x'] = 1600  
                    obstacle['hitbox'].x = 1600 
                if obstacle['type'] == 'clif':
                    obstacle['x'] = 3600
                    obstacle['hitbox'].x = 3600
                if obstacle['type'] == 'nuddle':
                    obstacle['x'] = 3600
                    obstacle['hitbox'].x = 3600
    def draw(self):
        for obstacle in self.obstacles:
            self.window.blit(obstacle['image'], (obstacle['x'] , obstacle['y'] ))
            pygame.draw.rect(self.window, (255, 0, 0), obstacle['hitbox'], 2)
            
                
            
# Inicializando e rodando o jogo
game = Game()
nave = Nave(game.window, width=150, height=100)
obstacles = Obstacle(game.window)
obstacles.initialize_obstacle('platform', 980, 850)
obstacles.initialize_obstacle('platform', 1780, 850)
obstacles.initialize_obstacle('platform', 2580, 850)
obstacles.initialize_obstacle('clif', 1380, 410, width=200, height=600)
obstacles.initialize_obstacle('nuddle', 1380, 110, width=200, height=200)
obstacles.initialize_obstacle('nuddle', 1980, 110, width=200, height=400)
obstacles.initialize_obstacle('clif', 2380, 410, width=200, height=700)
obstacles.initialize_obstacle('nuddle', 2980, 10, width=200, height=200)
obstacles.initialize_obstacle('nuddle', 2980, 110, width=200, height=200)
obstacles.initialize_obstacle('clif', 2980, 210, width=200, height=900)
obstacles.initialize_obstacle('clif', 3580, 90, width=200, height=600)
obstacles.initialize_obstacle('nuddle', 4480, 110, width=200, height=300)
obstacles.initialize_obstacle('clif', 4180, 410, width=200, height=700)
game.run()
