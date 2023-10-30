import pygame

class ExplosionAnimation:
    def __init__(self, window):  # Corrigido o nome do método
        self.load_images()
        self.window = window
        self.duration = 300 // len(self.images)
        self.start_time = pygame.time.get_ticks()

    def load_images(self):
        self.images = []
        for i in range(1, 5):
            image = pygame.image.load(f'imagens/explosao{i}.png')
            scaled_image = pygame.transform.scale(image, (200, 200))
            self.images.append(scaled_image)

    def update(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        self.current_image_index = elapsed_time // self.duration

        if elapsed_time > self.duration * len(self.images):
            
            return False  # A animação terminou

        return True  # A animação ainda está em execução

    def draw_explosion(self, nave):
        if self.current_image_index < len(self.images):
            self.image = self.images[self.current_image_index]
            self.window.blit(self.image, (nave.x - 30, nave.y - (100 + self.current_image_index * 6)  ))

    def draw_game_over_message(self):
        font = pygame.font.Font(None, 74)
        game_over_text = font.render('Você perdeu', True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        self.window.blit(game_over_text, text_rect)