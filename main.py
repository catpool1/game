import pygame
from random import randint
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
player = Player()
enemy1 = Enemy()
object1 = Object((500, 40), (80, 10))


# main cycle
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    # background
    screen.fill((255, 255, 255))


    if not player.is_collided(HEIGHT, object1.get_rect(HEIGHT)):
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


    # enemy
    # x, y = player.get_xy()
    # enemy1.move((x, y))
    # enemy1.blit(screen, HEIGHT)
    # if enemy1.is_collided(HEIGHT, player.get_rect(HEIGHT)):
    #     text_fps = font_hit.render(f'HIT!!!', True, (0, 0, 255))
    #     screen.blit(text_fps, (randint(25, WIDTH-25), randint(25, HEIGHT-25)))

    # player
    player.blit(screen, HEIGHT)

    # objects
    object1.blit(screen, HEIGHT)

    # display update
    text_fps = font_fps.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(text_fps, (WIDTH - 80, HEIGHT - 20))
    pygame.display.flip()
    clock.tick(60)