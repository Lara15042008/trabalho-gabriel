# trabalho-gabriel
import pygame

# inicializando o pygame
pygame.init()

# definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("janela simples")

# loop principal do jogo
running = True 
while running:
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
                running = False
  
    # Atualizar a tela
    pygame.display.flip()

# finalizar o pygame
pygame.quit() 
