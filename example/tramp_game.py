import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("САМАЯ КРУТАЯ ИГРА В МИРЕ!!!!!")
x = 250
y = 427
speed = 5
isjump = False
jumpcount = 10


left = False
right = False
animCount = 0

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

bullets = []
lastmove = "right"

walkRight = [pygame.image.load('pygame_right_1.png'), pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'),
             pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'),
             pygame.image.load('pygame_right_6.png')]

walkLeft = [pygame.image.load('pygame_left_1.png'), pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'),
            pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'), pygame.image.load('pygame_left_6.png'),
            pygame.image.load('pygame_left_1.png')]

playerStand = pygame.image.load('pygame_idle.png')

bg = pygame.image.load('bg.jpg')

width = 60
height = 71

clock = pygame.time.Clock()
def draw_window():
    global animCount
    screen.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        screen.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        screen.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
         screen.blit(playerStand, (x, y))
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.flip()

while True:
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index((bullet)))


    clock.tick(30)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > -7:
        x -= speed
        left = True
        right = False
        lastmove = "left"
    elif keys[pygame.K_RIGHT] and x < 450:
        x += speed
        left = False
        right = True
        lastmove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not (isjump):
        # if keys[pygame.K_UP] and y>25:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y<675:
        #         y += speed
        if keys[pygame.K_UP]:
            isjump = True
    else:
        if jumpcount >= -10:
            if jumpcount < 0:
                y += (jumpcount ** 2) / 2
            else:
                y -= (jumpcount ** 2) / 2
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10
    if keys[pygame.K_DOWN]:
        if lastmove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 9:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    draw_window()
