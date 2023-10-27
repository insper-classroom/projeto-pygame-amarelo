import pygame
from menu import *  
from obstaculo import *
from nave import *

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('Star Adventure')
        self.fundo = pygame.image.load('imagens/fundo_do_JR.png')
        self.fundo = pygame.transform.scale(self.fundo, (1600, 860))
        
        self.running = False
        self.clock = pygame.time.Clock()
        self.pontuação = 0 
        self.start_time = pygame.time.get_ticks()
    
    def run(self, obstacles, nave, menu):
         
        while menu.running:
            menu_result = menu.run()  # Aqui você pode passar a última e a melhor pontuação
            if menu_result:  # Se o resultado do menu for True (jogo deve começar)
                self.start_time = pygame.time.get_ticks()  # Resetar o tempo inicial

                self.running = True
                while self.running:
                    dt = self.clock.tick(60)/1000  # delta tempo em segundos.
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

            