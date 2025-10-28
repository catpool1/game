import pygame
from models.room_loading import room_load

# screen settings
pygame.init()
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])

is_jump: bool = False
hit: bool = False
jump_pause: bool = True

last_move = ''

# clock
clock = pygame.time.Clock()

# text
font_fps = pygame.font.SysFont("timesnewroman", 20)


# bugs:
# fall threw collisions:  5 - 6 / 24 - 27 / 41 - 45 // 148 - 152 / 178 - 180 / 260 - 360
# jump threw collisions on some pixels: 360 -> 440


# room load
level = room_load('test')
player = level[0]
enemies = level[1]
objects = level[2]
spikes = level[3]
levers = level[4]
exits = level[5]
backgrounds = level[6]


# main cycle
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_c]:
        print(player.get_xy())
    if keys[pygame.K_x]:
        player.tp((970, 400))
    if keys[pygame.K_f]:
        exits[0].result(player)
    if keys[pygame.K_ESCAPE]:
        exit()

    # background
    screen.fill((255, 255, 255))

    for bk in backgrounds:
        bk.blit(screen, HEIGHT)


    # enemies
    for en in enemies:
        en.blit(screen, HEIGHT)
        en.move(HEIGHT, objects)
        if en.is_collided(HEIGHT, player.get_rect(HEIGHT)):
            en.result(player)

    for sp in spikes:
        sp.blit(screen, HEIGHT)
        if sp.is_collided(HEIGHT, player.get_rect(HEIGHT)):
            sp.result(player)


    # objects
    for lv in levers:
        lv.blit(screen, HEIGHT)
        if lv.is_collided(HEIGHT, player.get_rect(HEIGHT)):
            lv.result()

    for ex in exits:
        ex.blit(screen, HEIGHT)
        if ex.is_collided(HEIGHT, player.get_rect(HEIGHT)):
            level = room_load(ex.room())
            player = level[0]
            enemies = level[1]
            objects = level[2]
            spikes = level[3]
            levers = level[4]
            exits = level[5]
            backgrounds = level[6]
            player.tp((50, 0))

    for obj in objects: # 4 'for' cycles with objects (that's bad)
        obj.blit(screen, HEIGHT)


    # player
    player.blit(screen, HEIGHT)
    player.move(HEIGHT, keys, objects)


    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)