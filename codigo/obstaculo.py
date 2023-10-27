import pygame


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
                