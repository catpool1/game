import pygame
# import json
from models.player import Player
from models.enemy import Enemy
from models.object import Object


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


# player model
player = Player() # 10 -> 192 jump height
enemies = [Enemy(pos=(780, 580)), Enemy(pos=(700, 340), speed_x=4),
           Enemy(pos=(1100, 0), direction='left'), Enemy(pos=(1300, 0), speed_x=6),
           Enemy(pos=(1315, 630), speed_x=0)]

# fall threw collisions:  5 - 6 / 24 - 27 / 41 - 45 // 148 - 152 / 178 - 180
# jump threw collisions on some pixels: 360 -> 440

objects = [Object((100, 170), (80, 22)),
           Object((1000, 600), (80, 60)), Object((500, 100), (80, 60)),
           Object((600, 200), (80, 60)), Object((700, 300), (180, 40)),
           Object((600, 440), (80, 60)), Object((780, 550), (200, 30)),
           Object((1100, 700), (80, 60)), Object((1200, 570), (80, 60)),
           Object((1300, 570), (80, 60)), Object((870, 330), (40, 40)),
           Object((1100, 50), (80, 60)), Object((1200, 50), (80, 60)),
           Object((700, 0), (80, 60)), Object((700, 70), (80, 60)),
           Object((1400, 400), (200, 30)),
           Object((-10, 0), (10, 900)), Object((1600, 0), (10, 900)),
           Object((0, -10), (2000, 10)), Object((0, 900), (2000, 10))]

# test = {}
# test['player'] = player.get_info()
# test['objects'] = []
# for obj in objects:
#     test['objects'].append(obj.get_info())
#
# with open('rooms/test.json', 'r+') as f:
#     json.dump(test, f, indent=4)

# main cycle
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_c]:
        print(player.get_xy())
    if keys[pygame.K_x]:
        player.tp((1200, 700))
    if keys[pygame.K_ESCAPE]:
        exit()

    # background
    screen.fill((255, 255, 255))


    # player
    player.blit(screen, HEIGHT)
    player.move(HEIGHT, keys, objects)

    # enemies
    for en in enemies:
        en.blit(screen, HEIGHT)
        en.move(HEIGHT, objects)
        if en.is_collided(HEIGHT, player.get_rect(HEIGHT)):
            player.tp((100, 0))


    # objects
    for obj in objects:
        obj.blit(screen, HEIGHT)

    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)