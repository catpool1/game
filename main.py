import pygame
from models.player import Player


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


# player model
player = Player(250, 0, 50, 50, 10)


# main cycle
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    # background
    screen.fill((255, 255, 255))

    # movement
    if keys[pygame.K_a] and keys[pygame.K_d]:
        pass

    elif keys[pygame.K_a]:
        player.move_left()

    elif keys[pygame.K_d]:
        player.move_right(WIDTH)


    # jumps
    if not is_jump:
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            is_jump = True

    else:
        if not player.jump():
            is_jump = False

    player.blit(screen, HEIGHT)

    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)