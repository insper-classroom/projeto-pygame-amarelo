import pygame
from nave import Nave


class ExplosionAnimation:
    def _init_(self, window):
        explosao_1 = pygame.image.load('imagens/explosao1.png')
        self.explosao_1 = pygame.transform.scale(explosao_1, (100, 100))
        explosao_2 = pygame.image.load('imagens/explosao2.png')
        self.explosao_2 = pygame.transform.scale(explosao_2, (100, 100))
        explosao_3 = pygame.image.load('imagens/explosao4.png')
        self.explosao_3 = pygame.transform.scale(explosao_3, (100, 100))
        explosao_4 = pygame.image.load('imagens/explosao5.png')
        self.explosao_4 = pygame.transform.scale(explosao_4, (100, 100))
        self.images = [
            explosao_1,
            explosao_2,
            explosao_3,
            explosao_4
        ]
        self.current_image_index = 0
        self.x = 0
        self.y = 0
        self.window = window
        self.duration = 3000 // len(self.images)
        self.start_time = pygame.time.get_ticks()

    def update(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time

        if elapsed_time > self.duration * len(self.images):
            return False  # A animação terminou

        self.current_image_index = elapsed_time // self.duration
        return True  # A animação ainda está em execução

    def draw_explosion(self, nave):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time < self.duration:
            # Escolha a imagem baseada no tempo decorrido
            if current_time - self.start_time < self.duration / 4:
                image = self.explosao_1
            elif current_time - self.start_time < self.duration / 2:
                image = self.explosao_2
            elif current_time - self.start_time < 3 * self.duration / 4:
                image = self.explosao_3
            else:
                image = self.explosao_4
            # Desenhe a imagem na posição da nave
            self.window.blit(image, (nave.x, nave.y))
    def draw_game_over_message(self):
        font = pygame.font.Font(None, 74)
        game_over_text = font.render('Você perdeu', True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        self.window.blit(game_over_text, text_rect)