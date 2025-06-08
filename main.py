import pygame
import json
from models.player import Player
from models.enemy import Enemy
from models.object import Object


# screen settings
pygame.init()
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])

is_jump: bool = False
hit: bool = False

last_move = ''

# clock
clock = pygame.time.Clock()

# text
font_fps = pygame.font.SysFont("timesnewroman", 20)


# player model
player = Player()
# enemy1 = Enemy()

objects = [Object((1000, 610), (80, 60)), Object((500, 100), (80, 60)),
           Object((600, 200), (80, 60)), Object((700, 300), (80, 60)),
           Object((800, 400), (80, 60)), Object((900, 500), (80, 60)),
           Object((1100, 700), (80, 60)), Object((1200, 570), (80, 60)),
           Object((1300, 570), (80, 60)), Object((200, 0), (80, 100)),
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


    # movement
    if keys[pygame.K_a] and keys[pygame.K_d]:
        last_move = ''
        player.move_speed_zeroing()

    elif keys[pygame.K_a]:
        if last_move != 'left':
            player.move_speed_zeroing()
            last_move = 'left'

        for obj in objects:
            if obj.is_on_left(player.get_move_count(), player.get_xy(), player.get_size()):
                player.move_left(True, obj.get_distance_left(player.get_xy()))
                break
        else:
            player.move_left()

    elif keys[pygame.K_d]:
        if last_move != 'right':
            player.move_speed_zeroing()
            last_move = 'right'

        for obj in objects:
            if obj.is_on_right(player.get_move_count(), player.get_xy(), player.get_size()):
                player.move_right(True, obj.get_distance_right(player.get_xy(), player.get_size()))
                break
        else:
            player.move_right()

    else:
        last_move = ''


    # jump and fall
    for obj in objects:
        if obj.is_under(HEIGHT, player.get_info()['fall_speed'], player.get_xy(), player.get_size()):
            player.fall_speed_zeroing()

            # jumps
            if not is_jump:
                if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                    is_jump = True

                player.fall(True, obj.get_distance_up(player.get_xy()))
            break

        if is_jump:
            if obj.is_upper(HEIGHT, player.get_jump_count(), player.get_xy(), player.get_size()):
                player.jump(True, obj.get_distance_down(player.get_xy(), player.get_size()))
                is_jump = False
    else:
        if not is_jump:
            player.fall()

    # continue jumping
    if is_jump:
        if not player.jump():
            is_jump = False


    # enemy
    # enemy1.move(player.get_xy())
    # enemy1.blit(screen, HEIGHT)
    # if enemy1.is_collided(HEIGHT, player.get_rect(HEIGHT)):
    #     print('player damaged')

    # player
    player.blit(screen, HEIGHT)

    # objects
    for obj in objects:
        obj.blit(screen, HEIGHT)

    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)