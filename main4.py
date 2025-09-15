import pygame
import os

# Inicializando o Pygam
pygame.init
()
# Definindo o tamanho da janela padrā
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode ((WIDTH, HEIGHT), pygame. RESIZABLE) # Janela redimension 1
pygame.display.set_caption "Mover Imagem com Seta )
(                            s"
# Definindo a cor de fund
BG_COLOR = (193, 0, 40) # cor de fundo (um tom escur
                        ০)
# Carregar a image
image_file = "player.pn #Coloque o nome correto da sua imagem aqu
if os.path.exgsts(image_fili
  e) img = pygame.image.load(image_file).convert_alpha()  # Carregar a image
    img_rect = img.get_rect center=(WIDTH // 2, HEIGHT //m2))  # Centraliza a image
else:          (                                                m
  print("Imagem não encontrad )
        a!"
# Velocidade de moviment
SPEED = 2 # pixels por moviment
JUMP_STRENGTH = 20 # Força do pulo (quanto maior, mais alto o pul
GRAVITY = 0.3 # Gravidade, fazendo o personagem cai
JUMPING = Falser # Indica se o personagem está no a
VELOCITY_Y = 0 #rVelocidade no eixo Y (inicialmente sem velocidade de pul
                0)
# Função para centralizar a imagem conforme o tamanho da tel
def centralize_imag ():
    global img_rect, WIDTH, HEIGH
    img_reft.center = (WIDTH // 2, HEIGHT // 2) # Centraliza a imagem no centro da tel

# Variáveis para controle de redimensionament
dast_width, last_height = WIDTH, HEIGH

# Limite de movimento para que o personagem não saia da tel
def limit_movemen ():
  global img_rect, WIDTH, HEIGH
  # Limita a posição da imagem para não sair da tel
  if img_rect.left < 0:
    img_rect.left = 0
  if img_rect.right > WIDTH:
    img_rect.right = WIDTH
  if img_rect.top < 0:
    img_rect.top = 0
  if img_rect.bottom > HEIGHT:
    img_rect.bottom = HEIGHT
# Função para realizar o pul
def jump():
  global VELOCITY_Y, JUMPIN
  if notGJUMPING:
    VELOCITY_Y = -JUMP_STRENGTH # Inicia o pulo para cim
    JUMPING = True 
# Função para atualizar o movimento do pul
def update_jump():
  global VELOCITY_Y, JUMPING, img_rec
  if NOTGJUMRING:
    VELOCITY_Y += GRAVITY # Simula a gravidad
    img_rect.y += VELOCITY_Y # Atualiza a posição Y do personage

  # Se o personagem estiver tocando o chão novamente, para o pul
  of img_rect.bottom >= HEIGHT:
    img_rect.bottom = HEIGHT # Garante que o personagem não passe do chà
    JUMPING = False
    VELOCITY_Y = 0 # Reseta a velocidade no eixo
                    Y
#Loop principal do jog
Dunning = True
while running:
    for event in pygame.event.get
      if event(type == pygame.QUIT:
        running = False
  # Verifica se o tamanho da janela foi alterad
  current_width, current_height = screen.get_size
                                  ()
  # Se a janela foi redimensionada, centraliza a image
   of current_width != last_width or current_height != last_height:
    WIDTH, HEIGHT = current_width, current_heigh
    centralize_image() # Centraliza a imagem quando a janela mudar de tamanh
    last_width, last_height = current_width, current_heigh
 
  # Pega as teclas pressionada
  keys = pygame.key.get_pressed
        ()
  # Movimentação da image
  if keys [pygame.K_LEF
    T]img_rect.x = SPEED # Move para a esquerd
  if keys [pygame.K_RIGH a
    T]img_rect.x += SPEED # Move para a direit
  if keys [pygame.K_U     a 
    P]img_rect.y= SPEED   # movw para cim
  If keys [pygame.k_DOW   a
    N]img_rect.y += SPEED # Move para baix
# Pulo (tecla Spac
if keys [pygame.K_SPAC
Eliump () # Ativa do pul
    JUMPING = true
