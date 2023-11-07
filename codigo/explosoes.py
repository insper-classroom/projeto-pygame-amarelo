import pygame

class ExplosionAnimation:
    """
    Inicializa a animação de explosão.
    pygame.Surface: A janela onde a animação será exibida.
    """
    def __init__(self, window):  # Corrigido o nome do método
        self.load_images()
        self.window = window
        self.duration = 300 // len(self.images)
        self.start_time = pygame.time.get_ticks()

    def load_images(self):
        """
        Carrega as imagens da animação de explosão.
        """
        self.images = []
        for i in range(1, 5):
            image = pygame.image.load(f'imagens/explosao{i}.png')
            scaled_image = pygame.transform.scale(image, (200, 200))
            self.images.append(scaled_image)

    def update(self):
        """
        Atualiza a animação de explosão.
        Return:
            True se a animação ainda está em execução, False se terminou.
        """
        elapsed_time = pygame.time.get_ticks() - self.start_time
        self.current_image_index = elapsed_time // self.duration

        if elapsed_time > self.duration * len(self.images):
            
            return False  # A animação terminou

        return True  # A animação ainda está em execução

    def draw_explosion(self, nave):
        """
        Desenha a explosão na posição da nave.
        nave: A instância da nave onde a explosão deve ser exibida.
        """
        if self.current_image_index < len(self.images):
            self.image = self.images[self.current_image_index]
            self.window.blit(self.image, (nave.x - 30, nave.y - (100 + self.current_image_index * 6)  ))
    
    