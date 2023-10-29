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
    obstacles.initialize_obstacle('nuddle', random.randint(4380, 4480), 110, width=100, height=500)
    obstacles.initialize_obstacle('clif', 4680, 510, width=100, height=500)
    game.run( obstacles, nave, menu, ExplosionAnimation)