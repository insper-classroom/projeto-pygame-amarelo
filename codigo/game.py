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
        self.fundo_2 = pygame.image.load('imagens/fundo_2.png')
        self.fundo_2 = pygame.transform.scale(self.fundo_2, (1600, 860))
        self.fundo_3 = pygame.image.load('imagens/fundo_3.png')
        self.fundo_3 = pygame.transform.scale(self.fundo_3, (1600, 860))
        self.game_over_background = pygame.image.load('imagens/game_over.png')
        self.game_over_background = pygame.transform.scale(self.game_over_background, (1600, 860))

        self.lista_fundo = [self.fundo, self.fundo_2, self.fundo_3]
        self.selected_background = random.choice(self.lista_fundo)
        self.game_over = False
        self.running = False
        self.clock = pygame.time.Clock()
        self.pontuação = 0 
        self.start_time = pygame.time.get_ticks()
        self.explosion_animation = ExplosionAnimation(self.window)
        self.contagem = 0
        self.obstacles = Obstacle(self.window)
        self.contagem_2 = 0
        # musica
        pygame.mixer.init()
        pygame.mixer.music.load('sons/the-asteroid-field.mp3')
        pygame.mixer.music.play(-1)
    
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
                        morreu = pygame.time.get_ticks()
                        while True:  # Loop de pós-colisão

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT or \
                                (event.type == pygame.KEYDOWN and 
                                    (event.key == pygame.K_ESCAPE or event.key == pygame.K_KP_ENTER)):
                                    self.game_over = False
                                    self.running = False
                                    menu.running = False
                                    self.game_over = False
                                    return
                            if self.explosion_animation.update():  # Atualiza a animação
                                self.explosion_animation.draw_explosion(nave)  # Desenha a animação
                            else:
                                break  # Se a animação terminou, sai do loop

                            pygame.display.flip()  # Atualiza a tela

                        self.window.blit(self.game_over_background, (180, 110))
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
                            pygame.display.flip()
                            
                            
                        for obstacle in obstacles.obstacles:
                            if not obstacle['type'] == 'platform': 
                                if nave.x > obstacle['x'] + obstacle['hitbox'].width and not obstacle['passed']:
                                    self.pontuação += 0.5 # Incremente a pontuação
                                    obstacle['passed'] = True
                                if obstacle['x'] > nave.x:
                                    obstacle['passed'] = False
                        # Atualizar objetos do jogo aqui
                       
                        self.window.blit(self.selected_background, (180, 110))
                        obstacles.update()
                        obstacles.draw()
                        nave.update(obstacles)
                        nave.draw()
            
                            
                        # Desenhar a pontuação
                        font = pygame.font.Font(None, 36)
                        score_text = font.render(f'Pontos: {int(self.pontuação)}', True, (255, 255, 255 ))
                        self.window.blit(score_text, (200, 160))
                        pygame.display.flip()
                    
                        

            