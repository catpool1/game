import math

import time

import pygame

pygame.init()
HEIGHT = 900
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.image.load('track.png')
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
MENU = pygame.image.load("track.png")
MENU = pygame.transform.scale(MENU, (WIDTH, HEIGHT))
f1 = pygame.font.Font(None, 36)
with open('records.txt') as file:
    best = min([float(x) for x in file])

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

last_win = None

# def rotate(image, rect, angle):
#     """Rotate the image while keeping its center."""
#     # Rotate the original image without modifying it.
#     new_image = pygame.transform.rotate(image, angle)
#     # Get a new rect with the center of the old rect.
#     rect = new_image.get_rect(center=rect.center)
#     return new_image, rect
#
# class igrok:
#     def __init__(self, width, height, x, y):
#         image = pygame.image.load('me.png')
#         self.speed_x = 0
#         self.speed_y = 0
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.image = pygame.transform.scale(image, (self.width, self.height))
#
#     def blit(self, screen):
#         screen.blit(self.image, (self.x - self.width // 2,
#                                  self.y - self.height // 2))
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = scale_image(pygame.image.load("me.png"), 0.2)
        #self.img = pygame.transform.rotate(img, 90)
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 90
        self.x, self.y = 641, 73
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_back(self):
        self.vel = min(self.vel - self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

class Playr2(AbstractCar):
    def __init__(self, max_vel, rotation_vel):
        super().__init__(max_vel, rotation_vel)
        self.x, self.y = 612, 35
        self.img = scale_image(pygame.image.load("vrag.png"), 0.2)


start = False
igroc = AbstractCar(5, 4)
igroc2 = Playr2(5, 4)
font = pygame.font.SysFont("Comic Sans", 72)
mytext = font.render('СТАРТ', True, (255, 255, 255))
mytext1 = font.render('ВЫХОД', True, (255, 255, 255))
prepare_time = 0

def start_menu():
    global start, poryadok, poryadok2, last_win, prepare_time, igroc, igroc2
    while not start:
        with open('records.txt') as file:
            best = min([float(x) for x in file])
        screen.blit(MENU, (0, 0))
        if last_win:
            pygame.draw.rect(screen, (100, 100, 100), (WIDTH // 2 - 365, HEIGHT // 2 - 130, 721, 50), width=5)
            pygame.draw.rect(screen, (100, 100, 100), (WIDTH // 2 - 365, HEIGHT // 2 - 130, 720, 49))
            color = (0, 0, 255) if last_win[:13] == 'Синий попедил' else (255, 255, 0)
            mytext2 = font.render(last_win, True, color)
            screen.blit(mytext2, (WIDTH // 2 - 360, HEIGHT // 2 - 130))
        mytext4 = font.render(str(best), True, (0, 0, 0))
        screen.blit(mytext4, (WIDTH // 2, 820))
        pygame.draw.rect(screen, (100, 100, 100), (WIDTH // 2 - 150, HEIGHT // 2 - 60, 275, 245))
        pygame.draw.rect(screen, (100, 100, 100), (WIDTH // 2 - 150, HEIGHT // 2 - 60, 275, 245), width=5)
        pygame.draw.rect(screen, (0, 127, 0), (WIDTH // 2 - 120, HEIGHT // 2, 215, 50))
        pygame.draw.rect(screen, (0, 127, 0), (WIDTH // 2 - 120, HEIGHT // 2, 215, 50), width=5)
        pygame.draw.rect(screen, (0, 127, 0), (WIDTH // 2 - 120, HEIGHT // 2 + 100, 215, 50))
        pygame.draw.rect(screen, (0, 127, 0), (WIDTH // 2 - 120, HEIGHT // 2 + 100, 215, 50), width=5)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
        x, y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed(num_buttons=3)
        if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 65 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
            pygame.draw.rect(screen, (0, 127, 127), (WIDTH // 2 - 120, HEIGHT // 2, 215, 50))
            if mouse[0] == True:
                prepare_time = time.time()
                poryadok = 0
                poryadok2 = 0
                igroc = AbstractCar(5, 4)
                igroc2 = Playr2(5, 4)
                start = True

        if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 200 and HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 150:
            pygame.draw.rect(screen, (0, 127, 127), (WIDTH // 2 - 120, HEIGHT // 2 + 100, 215, 50))
            if mouse[0] == True:
                exit()
        screen.blit(mytext, (WIDTH // 2 - 93, HEIGHT // 2))
        screen.blit(mytext1, (WIDTH // 2 - 113, HEIGHT // 2 + 100))
        pygame.display.flip()


angle = 0
hitboxes = []
# pygame.draw.rect(screen, (0, 0, 0), (450, 35, 100, 100))
hitboxes.append(pygame.rect.Rect(450, 35, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (205, 400, 100, 100))
hitboxes.append(pygame.rect.Rect(205, 400, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (80, 35, 100, 100))
hitboxes.append(pygame.rect.Rect(80, 35, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (20, 450, 100, 100))
hitboxes.append(pygame.rect.Rect(20, 450, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (325, 755, 100, 100))
hitboxes.append(pygame.rect.Rect(325, 755, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (500, 485, 100, 100))
hitboxes.append(pygame.rect.Rect(500, 485, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (700, 755, 100, 100))
hitboxes.append(pygame.rect.Rect(700, 755, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (770, 370, 100, 100))
hitboxes.append(pygame.rect.Rect(770, 370, 100, 100))
# pygame.draw.rect(screen, (0, 0, 0), (400, 300, 100, 100))
hitboxes.append(pygame.rect.Rect(400, 300, 100, 100))
hitboxes.append(pygame.rect.Rect(770, 130, 100, 100))
hitboxes.append(pygame.rect.Rect(560, 35, 20, 100))

poryadok = 0
poryadok2 = 0

running = True
# orig = igroc.image
# rect = igroc.image.get_rect(center=(350, 500))
# image = igroc.image
while running:
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moved = False
    moved2 = False
    rsg = 4 - time.time() + prepare_time

    if rsg < 0:
        if keys[pygame.K_j] and keys[pygame.K_RSHIFT]:
            poryadok = 11
        if keys[pygame.K_a]:
            igroc.rotate(left=True)
        if keys[pygame.K_d]:
            igroc.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            igroc.move_forward()
        if keys[pygame.K_s]:
            moved = True
            igroc.move_back()

        if not moved:
            igroc.reduce_speed()

        if keys[pygame.K_LEFT]:
            igroc2.rotate(left=True)
        if keys[pygame.K_RIGHT]:
            igroc2.rotate(right=True)
        if keys[pygame.K_UP]:
            moved2 = True
            igroc2.move_forward()
        if keys[pygame.K_DOWN]:
            moved2 = True
            igroc2.move_back()

        if not moved2:
            igroc2.reduce_speed()

    screen.blit(BG, (0, 0))
    if rsg >= 0:
        mytext2 = font.render(str(int(rsg)), True, (0, 0, 0))
        screen.blit(mytext2, (WIDTH // 2, HEIGHT // 2))
    else:
        mytext3 = font.render(str(abs(rsg))[:4], True, (0, 0, 0))
        screen.blit(mytext3, (50, 820))

    igroc.draw(screen)
    igroc2.draw(screen)
    if poryadok != 11:
        pygame.draw.circle(screen, (0, 0, 255), (hitboxes[poryadok].x + 50, hitboxes[poryadok].y + 70), 20)
        pygame.draw.circle(screen, (255, 255, 0), (hitboxes[poryadok2].x + 50, hitboxes[poryadok2].y + 30), 20)
    hitbox1 = pygame.rect.Rect((igroc.x, igroc.y + 15, 30, 30))
    hitbox2 = pygame.rect.Rect((igroc2.x, igroc2.y + 15, 30, 30))
    if hitbox1.collidelist(hitboxes) == poryadok:
        poryadok += 1
    if poryadok == 11:
        with open('records.txt', 'a') as file:
            file.write('\n' + str(abs(rsg))[:4])
        start = False
        last_win = 'Синий попедил. ВРЕМЯ ' + str(abs(rsg))[:4]
        start_menu()
    if hitbox2.collidelist(hitboxes) == poryadok2:
        poryadok2 += 1
    if poryadok2 == 11:
        with open('records.txt', 'a') as file:
            file.write('\n' + str(abs(rsg))[:4])
        start = False
        last_win = 'Жёлтый победил. ВРЕМЯ ' + str(abs(rsg))[:4]
        start_menu()
    # pygame.draw.rect(screen, (0, 0, 0), (igroc.x, igroc.y + 15, 30, 30))
    pygame.display.flip()
    pygame.time.delay(10)
