import pygame
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])

body_width: int = 50
body_height: int = 50

move_x_limit = body_width//2
move_y_limit = body_height//2

x: int = 250
y: int = HEIGHT-body_height//2

speed: int = 10
is_jump: bool = False
jump_height: int = 10

left: bool = False
right: bool = False

clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25, 25)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        pass

    elif keys[pygame.K_LEFT] and x > move_x_limit:
        if x - speed < move_x_limit:
            x = move_x_limit
        else:
            x -= speed

    elif keys[pygame.K_RIGHT] and x < WIDTH - move_x_limit:
        if x + speed > WIDTH - move_x_limit:
            x = WIDTH - move_x_limit
        else:
            x += speed


    pygame.display.flip()
    clock.tick(60)