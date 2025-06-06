import pygame

# screen settings
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# character settings
body_width: int = 50
body_height: int = 50

move_x_limit: int = body_width//2
move_y_limit: int = body_height//2

x: int = 250
y: int = move_y_limit

move_speed: int = 10

is_jump: bool = False
jump_limit: int = 10
jump_count: int = jump_limit

left: bool = False
right: bool = False

# clock
clock = pygame.time.Clock()

# text
font_fps = pygame.font.SysFont("timesnewroman", 20)


# main cycle
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    # background
    screen.fill((255, 255, 255))

    # character
    pygame.draw.circle(screen, (255, 0, 0), (x, HEIGHT-y), 25, 25)

    # movement
    if keys[pygame.K_a] and keys[pygame.K_d]:
        pass

    elif keys[pygame.K_a] and x > move_x_limit:
        if x - move_speed < move_x_limit:
            x = move_x_limit
        else:
            x -= move_speed

    elif keys[pygame.K_d] and x < WIDTH - move_x_limit:
        if x + move_speed > WIDTH - move_x_limit:
            x = WIDTH - move_x_limit
        else:
            x += move_speed


    # jumps
    if not is_jump:
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            is_jump = True

    else:
        if jump_count >= -jump_limit:
            if jump_count < 0:
                y -= (jump_count ** 2) / 2
            else:
                y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = jump_limit

    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)