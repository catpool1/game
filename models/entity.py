import pygame

class Entity:
    def __init__(self, x: int, y: int, width: int, height: int, speed_x: int, hp: int = 100, jump_height: int = 10, texture: str = r'resources\enemy_test.png'):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.width = width
        self.height = height
        self.hp = hp
        self.jump_height = jump_height
        texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(texture, (self.width, self.height))

    def blit(self, screen, height):
        screen.blit(self.texture, (self.x - self.width // 2,
                                 height - self.y - self.height))

    def get_xy(self):
        return self.x, self.y

    def is_collided(self, rect):
        r1 = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)

    def get_rect(self):
        return (self.x - self.width // 2, self.y - self.height // 2,
                self.width, self.height)