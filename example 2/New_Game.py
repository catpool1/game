import pygame
from random import randint


def calculate_speed(x1, y1, x2, y2, speed):
    dx = x2 - x1
    dy = y2 - y1
    d = (dx ** 2 + dy ** 2) ** 0.5
    speed_x = speed * (dx / d)
    speed_y = speed * (dy / d)
    return speed_x, speed_y


pygame.init()
HEIGHT = 900
WIDTH = 1600
MENU = pygame.image.load("28dayslater.jpg")
MENU = pygame.transform.scale(MENU, (WIDTH, HEIGHT))
BG_COLOR = 255, 255, 255
# BG = pygame.image.load('програм.jpg')
# bg = pygame.transform.scale(BG, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

f1 = pygame.font.Font(None, 36)
aptechka = 10
ecstr_apt = 2


class ball:
    def __init__(self, x1, y1, x2, y2, radius, image, speed):
        self.x = x1
        self.y = y1
        self.radius = radius
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (self.radius * 4, self.radius * 4))
        self.speed_x, self.speed_y = calculate_speed(x1, y1, x2, y2, speed)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def blit(self, screen):
        screen.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def is_out(self, width, height):
        if self.x + self.radius < 0:
            return True
        if self.y + self.radius < 0:
            return True
        if self.x - self.radius > width:
            return True
        if self.y - self.radius > height:
            return True

        return False

    def get_rect(self):
        return self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius


class Fireball(ball):
    def __init__(self, x1, y1, x2, y2, radius):
        super().__init__(x1, y1, x2, y2, radius, "fireball.png", 8)
        self.type = 'fire'


class iceball(ball):
    def __init__(self, x1, y1, x2, y2, radius):
        super().__init__(x1, y1, x2, y2, radius, "iceball.png", 4)
        self.type = 'ice'


class Wizard:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.width = width
        self.height = height
        image = pygame.image.load("cat.png")
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.HP = 100

    def blit(self, screen):
        screen.blit(self.image, (self.x - self.width // 2,
                                 self.y - self.height // 2))

    def move(self):
        if HEIGHT - 50 > self.y > 50:
            self.y += self.speed_y * 5
        elif self.y > 50:
            self.y = HEIGHT - 51
        else:
            self.y = 51
        if WIDTH - 50 > self.x > 50:
            self.x += self.speed_x * 5
        elif self.x > 50:
            self.x = WIDTH - 51
        else:
            self.x = 51

    def change_speed_y(self, speed_y):
        self.speed_y = speed_y

    def change_speed_x(self, speed_x):
        self.speed_x = speed_x

    def get_xy(self):
        return self.x, self.y

    def is_collided(self, rect):
        r1 = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)


class Enemy:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.hp = 100
        self.speed = 3
        self.width = width
        self.height = height
        image = pygame.image.load("zombie.png")
        self.image = pygame.transform.scale(image, (self.width, self.height))

    def move(self, x, y):
        self.speed_x, self.speed_y = calculate_speed(self.x, self.y, x, y, self.speed)

        self.x += self.speed_x
        self.y += self.speed_y

    def blit(self, screen):
        screen.blit(self.image, (self.x - self.width // 2,
                                 self.y - self.height // 2))

    def get_rect(self):
        return (self.x - self.width // 2, self.y - self.height // 2,
                self.width, self.height)

    def is_collided(self, rect):
        r1 = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2,
                         self.width, self.height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)


class super_enemy(Enemy):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.hp = 1000

class super_big_enemy(Enemy):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.hp = 5000


wiz = Wizard(WIDTH // 2, HEIGHT // 2, 160, 160)
balls = []
ehemy_list = [Enemy(randint(1, WIDTH), randint(1, HEIGHT), 100, 100) for x in range(10)]
timer = 0
t = 0
t1 = 0
dead_zombi = []
score = 0
tmr = 2
volna = 0
start = False

font = pygame.font.SysFont("Comic Sans", 72)
mytext = font.render('СТАРТ', True, (255, 255, 255))
mytext1 = font.render('ВЫХОД', True, (255, 255, 255))
while True:
    while not start:
        screen.blit(MENU, (0, 0))
        pygame.draw.rect(screen, (100, 100, 100), (WIDTH // 2 - 150, HEIGHT // 2 - 60, 275, 245))
        pygame.draw.rect(screen, (100, 100, 100), (WIDTH // 2 - 150, HEIGHT // 2 - 60, 275, 245), width=5)
        pygame.draw.rect(screen, (200, 0, 50), (WIDTH // 2 - 120, HEIGHT // 2, 215, 50))
        pygame.draw.rect(screen, (200, 0, 50), (WIDTH // 2 - 120, HEIGHT // 2, 215, 50), width=5)
        pygame.draw.rect(screen, (200, 0, 50), (WIDTH // 2 - 120, HEIGHT // 2 + 100, 215, 50))
        pygame.draw.rect(screen, (200, 0, 50), (WIDTH // 2 - 120, HEIGHT // 2 + 100, 215, 50), width=5)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        x, y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed(num_buttons=3)
        if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 75 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
            pygame.draw.rect(screen, (200, 100, 50), (WIDTH // 2 - 120, HEIGHT // 2, 215, 50))
            if mouse[0] == True:
                start = True
                wiz.HP = 100
                score = 0
                volna = 0
                timer = 0
                aptechka = 10
                ecstr_apt = 2
                ehemy_list = [Enemy(randint(1, WIDTH), randint(1, HEIGHT), 100, 100) for x in range(10)]
        if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 175 and HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 150:
            pygame.draw.rect(screen, (200, 100, 50), (WIDTH // 2 - 120, HEIGHT // 2 + 100, 215, 50))
        screen.blit(mytext, (WIDTH // 2 - 95, HEIGHT // 2))
        screen.blit(mytext1, (WIDTH // 2 - 110, HEIGHT // 2 + 100))
        pygame.display.flip()
    wiz.HP += 0.1
    clock.tick(60)
    text1 = f1.render('Жизни ' + str(int(wiz.HP)), True, (180, 0, 0))
    text2 = f1.render('Счет ' + str(score), True, (180, 0, 0))
    text3 = f1.render('Аптечки ' + str(aptechka), True, (180, 0, 0))
    text4 = f1.render('Большие аптечки ' + str(ecstr_apt), True, (180, 0, 0))
    text5 = f1.render('Волна ' + str(volna), True, (180, 0, 0))
    timer += 0.005
    t -= 0.05
    if t < 0:
        t = 0
    t1 -= 0.05
    if t1 < 0:
        t1 = 0
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                wiz_pos = wiz.get_xy()
                if t == 0:
                    balls.append(Fireball(wiz_pos[0], wiz_pos[1],
                                          mouse_pos[0], mouse_pos[1],
                                          15))
                    t = 1
            if e.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                wiz_pos = wiz.get_xy()
                if t1 == 0:
                    balls.append(iceball(wiz_pos[0], wiz_pos[1],
                                         mouse_pos[0], mouse_pos[1],
                                         15))
                    t1 = 1


        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                wiz.change_speed_y(-1)
            elif e.key == pygame.K_s:
                wiz.change_speed_y(1)
            if e.key == pygame.K_a:
                wiz.change_speed_x(-1)
            elif e.key == pygame.K_d:
                wiz.change_speed_x(1)
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w or e.key == pygame.K_s:
                wiz.change_speed_y(0)
            if e.key == pygame.K_a or e.key == pygame.K_d:
                wiz.change_speed_x(0)
            if e.key == pygame.K_e and aptechka > 0:
                wiz.HP += 10
                aptechka -= 1
            if e.key == pygame.K_q and ecstr_apt > 0:
                wiz.HP += 100
                ecstr_apt -= 1
    wiz.move()
    dead_balls = []
    screen.fill((255, 255, 255))
    # screen.blit(bg, (0, 0))
    for ball in balls:
        ball.move()
        if ball.is_out(WIDTH, HEIGHT):
            dead_balls.append(ball)
    for ball in dead_balls:
        i = balls.index(ball)
        del balls[i]
    if timer > tmr:
        volna += 1
        if volna % 3 == 0:
            ehemy_list.append(super_enemy(randint(1, WIDTH), randint(1, HEIGHT), 180, 180))
        if volna % 10 == 0:
            ehemy_list.append(super_big_enemy(randint(1, WIDTH), randint(1, HEIGHT), 250, 250))
        ehemy_list += [Enemy(randint(1, WIDTH), randint(1, HEIGHT), 100, 100) for x in range(10)]
        timer -= tmr
        tmr -= 0.03
    for ehemy in ehemy_list:
        other_zombie = ehemy_list[:]
        other_zombie.remove(ehemy)
        for zombi in other_zombie:
            if ehemy.is_collided(zombi.get_rect()):
                zombi.move(*wiz.get_xy())
                ehemy.blit(screen)
                break
        else:
            ehemy.move(*wiz.get_xy())
            ehemy.blit(screen)
        if wiz.is_collided(ehemy.get_rect()):
            if isinstance(Enemy, super_enemy):
                wiz.HP -= 10
            else:
                wiz.HP -= 0.1
            if wiz.HP <= 0:
                start = False
        for ball in balls:
            if ehemy.is_collided(ball.get_rect()):
                if ball.type == 'fire':
                    ehemy.hp -= 100
                elif ball.type == 'ice':
                    ehemy.speed -= 1
                if ehemy.speed <= 0.5:
                    ehemy.speed = 0.5
                dead_balls.append(ball)
                if ehemy.hp <= 0:
                    score += 1
                    dead_zombi.append(ehemy)
    for dead in dead_zombi:
        ehemy_list.remove(dead)
    dead_zombi = []
    dead_balls = list(set(dead_balls))
    for ball in dead_balls:
        try:
            i = balls.index(ball)
            del balls[i]
        except:
            pass

    for ball in balls:
        ball.blit(screen)
        # pygame.draw.circle(screen, (0, 0, 0), (ball.x, ball.y), 5)
    wiz.blit(screen)
    # wiz_pos = wiz.get_xy()
    # pygame.draw.circle(screen, (0, 0, 0), wiz_pos, 5)
    screen.blit(text1, (100, 50))
    screen.blit(text2, (100, 100))
    screen.blit(text3, (100, 150))
    screen.blit(text4, (100, 200))
    screen.blit(text5, (100, 250))
    pygame.display.update()
