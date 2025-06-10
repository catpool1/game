import pygame
# import json
from models.player import Player
# from models.enemy import Enemy
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
player = Player()

objects = [Object((1000, 600), (80, 60)), Object((500, 100), (80, 60)),
           Object((600, 200), (80, 60)), Object((700, 300), (80, 60)),
           Object((800, 400), (80, 60)), Object((900, 500), (80, 60)),
           Object((1100, 700), (80, 60)), Object((1200, 570), (80, 60)),
           Object((1300, 570), (80, 60)), Object((200, 0), (80, 100)),
           Object((1100, 50), (80, 60)), Object((1200, 50), (80, 60)),
           Object((700, 0), (80, 60)), Object((700, 70), (80, 60)),
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

    # background
    screen.fill((255, 255, 255))


    # player
    player.blit(screen, HEIGHT)

    # player movement
    player.move(HEIGHT, keys, objects)


    # objects
    for obj in objects:
        obj.blit(screen, HEIGHT)

    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)