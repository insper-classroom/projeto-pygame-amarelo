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

    # Gera as plataformas
    obstacles.initialize_obstacle('platform', 180, 850)
    obstacles.initialize_obstacle('platform', 980, 850)
    obstacles.initialize_obstacle('platform', 1780, 850)
    

    # Gera pares de obstáculos 'clif' e 'nuddle' com uma lacuna de 200 pixels entre eles
    gap_size = 300  # O tamanho do espaço que a nave pode passar
    x_positions = [1380, 1780, 2180, 2680, 3080, 3480, 3880, 4280, 4680]  # Posições iniciais dos obstáculos
    for x in x_positions:
        obstacles.generate_obstacle_pair('clif', gap_size, x)
        #obstacles.generate_obstacle_pair('nuddle', gap_size, x)

    game.run(obstacles, nave, menu, explosion_animation)