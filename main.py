import pygame
import json
from models.player import Player
from models.enemy import Enemy
from models.object import Object
from models.spike import Spike
from models.exit import Exit
from models.lever import Lever


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

# fall threw collisions:  5 - 6 / 24 - 27 / 41 - 45 // 148 - 152 / 178 - 180 / 260 - 360
# jump threw collisions on some pixels: 360 -> 440


# reading room stats
with open('rooms/test.json', 'r') as f:
    js = json.load(f)

player = Player(js['player']['speed_x'], js['player']['fall_speed'], js['player']['jump_height'], js['player']['direction'],
                js['player']['hp'], js['player']['pos'], js['player']['size'], js['player']['texture_name'])

enemies = []
for en in js['enemies']:
    enemies.append(Enemy(en['speed_x'], en['fall_speed'], en['jump_height'], en['direction'],
                         en['hp'], en['pos'], en['size'], en['texture_name']))

objects = []
for obj in js['objects']:
    objects.append(Object(obj['pos'], obj['size'], obj['texture']))

spikes = []
for sp in js['spikes']:
    spikes.append(Spike(sp['pos'], sp['size'], sp['texture']))

levers = []
for lv in js['levers']:
    for obj in objects:
        if obj.get_info()['pos'] == tuple(lv['door_pos']):
            levers.append(Lever(obj, lv['pos'], lv['size'], lv['texture'], lv['switched_texture']))

exit_room = Exit(js['exit']['pos'], js['exit']['size'], js['exit']['texture'])


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
        exit_room.result(player)
    if keys[pygame.K_ESCAPE]:
        exit()

    # background
    screen.fill((255, 255, 255))


    # enemies
    # for en in enemies:
    #     en.blit(screen, HEIGHT)
    #     en.move(HEIGHT, objects)
    #     if en.is_collided(HEIGHT, player.get_rect(HEIGHT)):
    #         en.result(player)

    for sp in spikes:
        sp.blit(screen, HEIGHT)
        if sp.is_collided(HEIGHT, player.get_rect(HEIGHT)):
            sp.result(player)


    # objects
    for lv in levers:
        lv.blit(screen, HEIGHT)
        if lv.is_collided(HEIGHT, player.get_rect(HEIGHT)):
            lv.result()

    exit_room.blit(screen, HEIGHT)
    if exit_room.is_collided(HEIGHT, player.get_rect(HEIGHT)):
        exit_room.result(player)

    for obj in objects:
        obj.blit(screen, HEIGHT)


    # player
    player.blit(screen, HEIGHT)
    player.move(HEIGHT, keys, objects)


    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)