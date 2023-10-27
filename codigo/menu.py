import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        self.running = True
        self.menu_image = pygame.image.load('imagens/Tela_inicial.png')  # Carregue sua imagem de fundo aqui
        self.menu_image = pygame.transform.scale(self.menu_image, (1600, 860))
        self.font = pygame.font.Font(None, 74)
        self.start_button = pygame.Rect(860, 540, 200, 80)  # Ajuste as coordenadas e o tamanho conforme necessário
        
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:  # Verifica se alguma tecla foi pressionada
                    if event.key == pygame.K_SPACE:  # Verifica se a tecla pressionada é a barra de espaço
                        return True  # Retorna True para iniciar o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.window.blit(self.menu_image, (180, 110))  # Desenhar a imagem do menu

            pygame.display.flip()