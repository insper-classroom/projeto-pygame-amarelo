
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
        clock = pygame.time.Clock()  #relógio para controlar a taxa de quadros por segundo
        nave = Nave(self.window, width=100, height=100)
        obstacles = Obstacle(self.window)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.running = False

            collision_detected = nave.update(obstacles)
            if collision_detected:
                self.running = False

            self.window.blit(self.fundo, (180, 110))
            obstacles.update()
            obstacles.draw()
            nave.update(obstacles)
            nave.draw()

            pygame.display.flip()
            clock.tick(60)  # Limita a taxa de quadros a 60 por segundo

class Nave:
    def __init__(self, window, width=None, height=None):
        self.window = window
        self.image = pygame.image.load('imagens/nave.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = 400
        self.y = 300
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, obstacles):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.hitbox.top > 0:
            self.y -= 5
        if keys[pygame.K_DOWN] and self.hitbox.bottom < 1080:
            self.y += 5
        self.hitbox.y = self.y

        for obstacle in obstacles.obstacles:
            if self.hitbox.colliderect(obstacle['hitbox']):
                return True
        return False

    def draw(self):
        self.window.blit(self.image, self.hitbox.topleft)
        pygame.draw.rect(self.window, (255, 0, 0), self.hitbox, 2)

class Obstacle:
    def __init__(self, window):
        self.window = window
        self.obstacles = []

        # Inicialize os obstáculos aqui
        self.initialize_obstacle('platform', 980, 850)
        self.initialize_obstacle('platform', 1780, 850)
        self.initialize_obstacle('platform', 2580, 850)
        self.initialize_obstacle('clif', 1380, 410, width=200, height=600)
        self.initialize_obstacle('nuddle', 1380, 110, width=200, height=200)
        self.initialize_obstacle('nuddle', 1980, 110, width=200, height=400)
        self.initialize_obstacle('clif', 2380, 410, width=200, height=700)
        self.initialize_obstacle('nuddle', 2980, 110, width=200, height=200)
        self.initialize_obstacle('clif', 2980, 210, width=200, height=900)
        self.initialize_obstacle('clif', 3580, 90, width=200, height=600)
        self.initialize_obstacle('nuddle', 4480, 110, width=200, height=300)
        self.initialize_obstacle('clif', 4180, 410, width=200, height=700)

    def initialize_obstacle(self, obstacle_type, x, y, width=None, height=None):
        obstacles = {
            'platform': 'imagens/plataforma.png',
            'clif': 'imagens/obstaculo.png',
            'nuddle': 'imagens/obstaculo_ceu.png'
        }

        image = pygame.image.load(obstacles[obstacle_type])

        if width and height:
            image = pygame.transform.scale(image, (width, height))

        if obstacle_type == 'clif':
            hitbox = image.get_rect(topleft=(x + image.get_width() * 0.15, y + image.get_height() * 0.20))
        else:
            hitbox = image.get_rect(topleft=(x + image.get_width() * 0.1, y + image.get_height() * 0.1))

        obstacle_images = {
            'type': obstacle_type,
            'x': x,
            'y': y,
            'image': image,
            'hitbox': hitbox
        }
        self.obstacles.append(obstacle_images)

    def update(self):
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
            self.window.blit(obstacle['image'], obstacle['hitbox'].topleft)
            pygame.draw.rect(self.window, (255, 0, 0), obstacle['hitbox'], 2)

game = Game()
game.run()


