import pygame
import random

class Obstacle:
    def __init__(self, window):
        """
        Classe que representa os obstaculos.
        pygame.Surface: A superfície da janela do jogo.
        """
        self.score = 0
        self.window = window
        self.obstacles = []
        self.passed = False
        self.obstacles_passed = []
    
    
    def initialize_obstacle(self, obstacle_type, x, y, width=None, height=None):
        """
        Inicializa um obstáculo.
        obstacle_type: O tipo de obstáculo('platform', 'clif' ou 'nuddle').
        x: A posição x do obstáculo.
        y: A posição y do obstáculo.
        width: A largura do obstáculo.
        height: A altura do obstáculo.
        """
        obstacles = {
            'platform': 'imagens/plataforma.png',
            'clif': 'imagens/paredao_megasonico.png',
            'nuddle': 'imagens/paredao_megasonico.png'
        }
        image = pygame.image.load(obstacles[obstacle_type])

        if width and height: 
            image = pygame.transform.scale(image, (width, height))

        hitbox = image.get_rect(topleft=(x, y))
        

        obstacle_images = {
            'type': obstacle_type,
            'x': x,
            'y': y,
            'image': image,
            'hitbox': hitbox,
            'passed': False,
        }
        obstacle_images['mask'] = pygame.mask.from_surface(obstacle_images['image'])
        self.obstacles.append(obstacle_images)

    def generate_obstacle_pair(self, obstacle_type, gap_size, x_position):
        """
        Gera um par de obstáculos com uma lacuna entre eles.
        obstacle_type: O tipo de obstáculo ('clif' ou 'nuddle').
        gap_size: O tamanho do espaço entre os obstáculos superior e inferior.
        x_position: A posição x inicial para os obstáculos.
        """
        width = 100  # Largura padrão para os obstáculos 'clif' e 'nuddle'
        total_height = self.window.get_height()

        # A altura do obstáculo de baixo é aleatória, mas deixa espaço para a lacuna e o obstáculo de cima
        bottom_height = random.randint(200, 700)  # 200 é um valor mínimo de exemplo para a altura do obstáculo superior

        # O obstáculo de baixo começa na parte inferior da tela menos sua altura
        bottom_y_position = total_height - bottom_height

        # O obstáculo de cima é o que resta do espaço menos a lacuna
        top_height = total_height - bottom_height - gap_size

        # O obstáculo de cima começa no topo da tela (y=0)
        top_y_position = 0

        # Inicializa o obstáculo inferior
        self.initialize_obstacle(obstacle_type, x_position, bottom_y_position, width, bottom_height)

        # Inicializa o obstáculo superior
        self.initialize_obstacle(obstacle_type, x_position, top_y_position, width, top_height)

    def update(self):
        """
        Atualiza a posição dos obstáculos na tela.
        """
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
        """
        Desenha os obstáculos na tela.
        """
        for obstacle in self.obstacles:
            self.window.blit(obstacle['image'], (obstacle['x'] , obstacle['y'] ))
            
                