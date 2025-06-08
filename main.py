import pygame
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

objects = [Object((204, 0), (80, 100)), Object((500, 60), (80, 60)),
           Object((600, 130), (80, 160)), Object((700, 330), (80, 140)),
           Object((800, 330), (80, 160)), Object((900, 430), (80, 160)),
           Object((-10, 0), (10, 900)), Object((1600, 0), (10, 900)),
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
            if obj.is_on_left(player.get_speed_x(), player.get_xy(), player.get_size()):
                player.move_left(True, obj.get_distance_left(player.get_xy()))
                print('object on left')
                break
        else:
            player.move_left()

    if keys[pygame.K_d]:
        for obj in objects:
            if obj.is_on_right(player.get_speed_x(), player.get_xy(), player.get_size()):
                player.move_right(True, obj.get_distance_right(player.get_xy(), player.get_size()))
                print('object on right')
                break
        else:
            player.move_right()

    # checking if player on object
    for obj in objects:
        if obj.is_under(HEIGHT, player.get_fall_speed(), player.get_xy(), player.get_size()):
            # jumps
            if not is_jump:
                if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                    is_jump = True
                    print('player jumped')

                player.fall_to_distance(obj.get_distance_up(player.get_xy()))
                print('player over object')
            break
    else:
        if not is_jump:
            player.fall()

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