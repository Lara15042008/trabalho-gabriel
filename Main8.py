        rect.right = WIDTH
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > HEIGHT:
        rect.bottom = HEIGHT

# Função para pular do jogador
def jump():
    global VELOCITY_Y, JUMPING
    if not JUMPING:
        VELOCITY_Y = -JUMP_STRENGTH
        JUMPING = True

# Atualiza o pulo do jogador
def update_jump():
    global VELOCITY_Y, JUMPING, img_rect, GRAVITY
    if JUMPING:
        VELOCITY_Y += GRAVITY
        img_rect.y += VELOCITY_Y
        if img_rect.bottom >= HEIGHT:
            img_rect.bottom = HEIGHT
            JUMPING = False
            VELOCITY_Y = 0

# Atualiza o pulo / queda do alvo chutado
def update_target_physics():
    global target_velocity_x, target_velocity_y, target_jumping, target_rect, target_gravity

    if target_jumping:
        target_velocity_y += target_gravity
        target_rect.x += target_velocity_x
        target_rect.y += target_velocity_y

        if target_rect.bottom >= HEIGHT:
            target_rect.bottom = HEIGHT
            target_jumping = False
            target_velocity_x = 0
            target_velocity_y = 0
        else:
            target_velocity_x *= 0.95

# Função para "chutar" o alvo
def kick():
    global target_velocity_x, target_velocity_y, target_jumping, target_rect, img_rect

    dist_x = target_rect.centerx - img_rect.centerx
    dist_y = target_rect.centery - img_rect.centery
    distancia = (dist_x ** 2 + dist_y ** 2) ** 0.5

    if distancia < 150:
        target_velocity_x = 20 if dist_x > 0 else -20
        target_velocity_y = -20
        target_jumping = True

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detectar redimensionamento
    current_width, current_height = screen.get_size()
    if current_width != last_width or current_height != last_height:
        WIDTH, HEIGHT = current_width, current_height

        # manter personagens no chão
        img_rect.bottom = HEIGHT
        target_rect.bottom = HEIGHT

        if background_orig:
            background = pygame.transform.scale(background_orig, (WIDTH, HEIGHT))
        last_width, last_height = current_width, current_height

    # Teclas pressionadas
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        img_rect.x += SPEED
    if keys[pygame.K_UP]:
        img_rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        img_rect.y += SPEED

    if keys[pygame.K_SPACE]:
        jump()
    if keys[pygame.K_f]:
        kick()

    limit_movement(img_rect)
    limit_movement(target_rect)

    update_jump()
    update_target_physics()

    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(BG_COLOR)

    if img:
        screen.blit(img, img_rect.topleft)
    else:
        pygame.draw.rect(screen, (255, 0, 0), img_rect)

    if target_img:
        screen.blit(target_img, target_rect.topleft)
    else:
        pygame.draw.rect(screen, (0, 255, 0), target_rect)

    pygame.display.flip()

pygame.quit()
