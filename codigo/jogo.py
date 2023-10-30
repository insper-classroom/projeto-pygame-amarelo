import pygame
import math
import random
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('Star Adventure')
        self.fundo = pygame.image.load('imagens/fundo_do_JR.png')
        self.fundo = pygame.transform.scale(self.fundo, (1600, 860))
        
        self.running = True
        self.clock = pygame.time.Clock()
        self.pontuação = 0 
        self.start_time = pygame.time.get_ticks()
    def run(self):
        while self.running:
            dt = self.clock.tick(60)/1000 # delta tempo em segundos.
            current_time = pygame.time.get_ticks()  # Obtenha o tempo atual
            elapsed_time = (current_time - self.start_time) / 1000  # Tempo decorrido em segundos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.running = False
            collision_detected = nave.update(obstacles)
            if collision_detected:
                self.running = False

            self.pontuação = (3 * elapsed_time) + (1.4 ** (elapsed_time * 0.6)) 
            # Atualizar objetos do jogo aqui
            self.window.blit(self.fundo, (180, 110))
            obstacles.update()
            obstacles.draw()
            nave.update(obstacles)
            nave.draw()
            # Desenhar a pontuação
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Pontos: {int(self.pontuação)}', True, (255, 255, 255 ))
            self.window.blit(score_text, (200, 160))

            pygame.display.flip()
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
class Obstacle:
    def __init__(self, window):
        self.window = window
        self.obstacles = []
    def initialize_obstacle(self, obstacle_type, x, y, width=None, height=None):
        obstacles = {
            'platform': 'imagens/plataforma.png',
            'clif': 'imagens/paredao_megasonico.png',
            'nuddle': 'imagens/paredao_megasonico.png'
        }
        image = pygame.image.load(obstacles[obstacle_type])
        # Apenas para redimensionar a imagem.
        if width and height: # Caso especificado a largura e altura na hora de iniciar o jogo.
            image = pygame.transform.scale(image, (width, height))

        hitbox = image.get_rect(topleft=(x, y))
        

        obstacle_images = {
            'type': obstacle_type,
            'x': x,
            'y': y,
            'image': image,
            'hitbox': hitbox,
        }
        obstacle_images['mask'] = pygame.mask.from_surface(obstacle_images['image'])
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
            #pygame.draw.rect(self.window, (255, 0, 0), obstacle['hitbox'], 2)
                
            
# Inicializando e rodando o jogo
game = Game()
nave = Nave(game.window, width=100, height=100)
obstacles = Obstacle(game.window)
obstacles.initialize_obstacle('platform', 180, 850)
obstacles.initialize_obstacle('platform', 980, 850)
obstacles.initialize_obstacle('platform', 1780, 850)
obstacles.initialize_obstacle('platform', 2580, 850)
obstacles.initialize_obstacle('clif', 1380, 510, width=100, height=500)
obstacles.initialize_obstacle('nuddle', 1380, -310, width=100, height=500)
obstacles.initialize_obstacle('nuddle', random.randint(1980, 2080), random.randint(80, 110), width=100, height=400)
obstacles.initialize_obstacle('clif', random.randint(2380, 2480), random.randint(510, 610), width=100, height=400)
obstacles.initialize_obstacle('nuddle', random.randint(2980, 3080), random.randint(-90, 10), width=100, height=400)       
obstacles.initialize_obstacle('clif', random.randint(3680, 3780),random.randint(10, 90), width=100, height=500)
obstacles.initialize_obstacle('nuddle', random.randint(4180, 4480), 110, width=100, height=500)
obstacles.initialize_obstacle('clif', 4180, 510, width=100, height=500)
game.run()
