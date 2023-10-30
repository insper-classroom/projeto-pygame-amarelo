import pygame
from menu import *  
from obstaculo import *
from nave import *
from explosoes import *

class Game:
    def __init__(self):
        """
        Inicializa o jogo.
        """
        pygame.init()
        self.window = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('Star Adventure')
        self.fundo = pygame.image.load('imagens/fundo_do_JR.png')
        self.fundo = pygame.transform.scale(self.fundo, (1600, 860))
        self.game_over = False
        self.running = False
        self.clock = pygame.time.Clock()
        self.pontuação = 0 
        self.start_time = pygame.time.get_ticks()
        self.explosion_animation = ExplosionAnimation(self.window)
        self.contagem = 0
  
        # musica
        pygame.mixer.init()
        pygame.mixer.music.load('codigo\musica 8bit.mp3')
        pygame.mixer.music.play()
    
    def run(self, obstacles, nave, menu, explosion_animation):
        """
        Executa o jogo.
        obstacles: Instância da classe Obstacle.
        nave: Instância da classe Nave.
        menu: Instância da classe Menu.
        explosion_animation: Instância da classe ExplosionAnimation.
        """
         
        while menu.running:
            menu_result = menu.run()  # Aqui você pode passar a última e a melhor pontuação
            if menu_result:  # Se o resultado do menu for True (jogo deve começar)
                self.start_time = pygame.time.get_ticks()  # Resetar o tempo inicial

                self.running = True
                while self.running:
                    if self.game_over:
                        while True:  # Loop de pós-colisão
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT or \
                                (event.type == pygame.KEYDOWN and 
                                    (event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE)):
                                    self.game_over = False
                                    self.running = False
                                    menu.running = False
                                    self.game_over = False
                                    return
                            if self.explosion_animation.update():  # Usando a instância criada no __init__
                                self.explosion_animation.draw_explosion(nave)
                                self.explosion_animation.draw_game_over_message()

                                pygame.display.flip()
                    
                       
                    else:

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
                            if self.contagem == 0:
                                self.contagem += 1
                                self.explosion_animation.start_time = pygame.time.get_ticks()
                            self.game_over = True
                            nave.update(obstacles)
                            nave.draw()
                            continue
                        if self.game_over:
                            if self.explosion_animation.update():  # Se a animação ainda estiver rodando
                                self.explosion_animation.draw_explosion(nave)
                                self.explosion_animation.draw_game_over_message()
                            pygame.display.flip()
                            
                            
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
                    
                        

            