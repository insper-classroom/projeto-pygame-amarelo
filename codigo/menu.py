import pygame

class Menu:
    def __init__(self, window):
        """
        Inicializa a classe Menu.
        pygame.Surface: A superfície da janela do jogo.
        titulo: O título do jogo a ser exibido no menu. Padrão é None.
        instruções: As instruções do jogo a serem exibidas no menu.
        """
        self.window = window
        self.running = True
        self.menu_image = pygame.image.load('imagens/Tela_inicial.png')
        self.menu_image = pygame.transform.scale(self.menu_image, (1600, 860))
        self.font = pygame.font.Font(None, 74)
        self.start_button = pygame.Rect(860, 540, 200, 80) 
        
        
    def run(self):
        """
        Executa o menu, aguardando a interação do jogador para iniciar o jogo ou sair.
        Return:
            True se o jogador escolher iniciar o jogo, False se o jogador escolher sair.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE: 
                        return True 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.window.blit(self.menu_image, (180, 110))

            pygame.display.flip()