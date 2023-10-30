import pygame

class Obstacle:
    def __init__(self, window):
        """
        Classe que representa os obstaculos.
        pygame.Surface: A superfície da janela do jogo.
        """
        self.window = window
        self.obstacles = []
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
        }
        obstacle_images['mask'] = pygame.mask.from_surface(obstacle_images['image'])
        self.obstacles.append(obstacle_images)
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
            
                