from game import Game
from nave import Nave
from obstaculo import Obstacle
from menu import Menu
from explosoes import ExplosionAnimation
import random

if __name__ == "__main__":
    game = Game()
    
    nave = Nave(game.window, width=100, height=100)
    obstacles = Obstacle(game.window)
    menu = Menu(game.window)
    explosion_animation = ExplosionAnimation(game.window)
    obstacles.initialize_obstacle('platform', 180, 850)
    obstacles.initialize_obstacle('platform', 980, 850)
    obstacles.initialize_obstacle('platform', 1780, 850)
    obstacles.initialize_obstacle('platform', 2580, 850)
    obstacles.initialize_obstacle('clif', 1380, 510, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 1380, -310, width=100, height=570)
    obstacles.initialize_obstacle('clif', 1780, 610, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 1780, -210, width=100, height=570)
    obstacles.initialize_obstacle('clif', 2180, 710, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 2180, -110, width=100, height=570)
    obstacles.initialize_obstacle('clif', 2680, 610, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 2680, -210, width=100, height=570)
    obstacles.initialize_obstacle('clif', 3080, 410, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 3080, -410, width=100, height=570)
    obstacles.initialize_obstacle('clif', 3480, 310, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 3480, -510, width=100, height=570)
    obstacles.initialize_obstacle('clif', 3880, 610, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 3880, -210, width=100, height=570)
    obstacles.initialize_obstacle('clif', 4280, 810, width=100, height=650)
    obstacles.initialize_obstacle('nuddle', 4280, -10, width=100, height=570)
    obstacles.initialize_obstacle('clif', 4680, 710, width=100, height=600)
    obstacles.initialize_obstacle('nuddle', 4680, -110, width=100, height=570)
    game.run(obstacles, nave, menu, explosion_animation)