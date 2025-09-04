import pygame
import os

# inicializando o pygame
pygame.init()

# definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("janela com imagem")

# definindo imagem a cor de fundo
BG_COLOR = (30, 30, 40) # COR DE FUNDO (UM TOM ESSCURO)

#carregar imagem
image_file = "player.png" # coloque o nome da sua imagem
if os.path.exists(image_file):
     img = pygame.image.load(image_file):
     img_rect = img.get_rect(center=(WIDTH // 2, HERGHT // 2 )) # CARREGAR A IMAGEM
else:
     print("imagem nao encontrada!")

# loop principal do jogo
running = True 
while running:
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
                running = False
  
    # preencha o fundo 
    screen.fill(BG_COLOR)

    # desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# finalizar o pygame
pygame.quit() 
