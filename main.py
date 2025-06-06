import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
x: int = 250
y: int = 427
speed: int = 5
is_jump: bool = False
jump_count: int = 10

left: bool = False
right: bool = False

width: int = 50
height: int = 50

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > -7:
        x -= speed
    elif keys[pygame.K_RIGHT] and x < 450:
        x += speed