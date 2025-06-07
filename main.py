import pygame
# from random import randint
from models.player import Player
from models.enemy import Enemy
from models.object import Object


# screen settings
pygame.init()
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])

is_jump: bool = False
hit: bool = False

# clock
clock = pygame.time.Clock()

# text
font_fps = pygame.font.SysFont("timesnewroman", 20)
font_hit = pygame.font.SysFont("comicsans", 100)


# player model
player = Player(speed_x=6, fall_speed=10)
enemy1 = Enemy()

objects = [Object((200, 100), (80, 200)), Object((500, 30), (80, 10)),
           Object((0, -10), (2000, 10))]


# main cycle
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    # background
    screen.fill((255, 255, 255))


    # movement
    if keys[pygame.K_a]:
        for obj in objects:
            if obj.is_collided_right(player.get_xy(), player.get_size()):
                print('player stopped on right')
                break
            elif obj.is_on_left(player.get_speed_x(), player.get_xy(), player.get_size()):
                player.move_left_to_distance(obj.get_distance_x_left(player.get_xy(), player.get_size()))
                print('player on right')
                break
        else:
            player.move_left()

    if keys[pygame.K_d]:
        for obj in objects:
            if obj.is_collided_left(player.get_xy(), player.get_size()):
                print('player stopped on left')
                break
            elif obj.is_on_right(player.get_speed_x(), player.get_xy(), player.get_size()):
                player.move_right_to_distance(obj.get_distance_x_right(player.get_xy()))
                print('player on left')
                break
        else:
            player.move_right(WIDTH)

    # if keys[pygame.K_a] and keys[pygame.K_d]:
    #     pass
    # elif keys[pygame.K_d]:
    #     player.move_right(WIDTH)

    # checking if player on object
    for obj in objects:
        if obj.is_collided_up(HEIGHT, player.get_xy(), player.get_size()):

            # jumps
            if not is_jump:
                if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                    is_jump = True
                    print('player jumped')
            break

        # if fall_speed > distance -> player fall threw
        elif obj.is_under(HEIGHT, player.get_fall_speed(), player.get_xy(), player.get_size()):
            if not is_jump:
                player.fall_to_distance(obj.get_distance_y_up(player.get_xy()))
                print('player over')
                break
    else:
        if not is_jump:
            player.fall()
            print('player fall')

    # continue jumping
    if is_jump:
        if not player.jump():
            is_jump = False
            print('player out of jump')


    # enemy
    # x, y = player.get_xy()
    # enemy1.move((x, y))
    # enemy1.blit(screen, HEIGHT)
    # if enemy1.is_collided(HEIGHT, player.get_rect(HEIGHT)):
    #     text_fps = font_hit.render('HIT!!!', True, (0, 0, 255))
    #     screen.blit(text_fps, (randint(25, WIDTH-25), randint(25, HEIGHT-25)))

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