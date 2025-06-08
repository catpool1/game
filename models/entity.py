import pygame
from pygame import SurfaceType


class Entity:
    def __init__(self, speed_x: int, fall_speed: int, jump_height: int, hp: int, pos: tuple, size: tuple, texture: str) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.speed_x = speed_x
        self.fall_speed = fall_speed
        self.width = size[0]
        self.height = size[1]
        self.hp = hp
        self.jump_height = jump_height
        texture = pygame.image.load(f'resources/{texture}.png')
        self.texture = pygame.transform.scale(texture, (self.width, self.height))

    def blit(self, screen: SurfaceType, screen_height: int) -> None:
        screen.blit(self.texture, (self.x,
                                 screen_height - self.y - self.height))

    def get_xy(self) -> tuple:
        return self.x, self.y

    def is_collided(self, screen_height: int, rect: tuple) -> bool:
        r1 = pygame.Rect(self.x, screen_height - self.y, self.width, self.height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)

    def get_rect(self, screen_height: int) -> tuple:
        return self.x, screen_height - self.y, self.width, self.height

    def get_size(self) -> tuple:
        return self.width, self.height

    def get_fall_speed(self) -> int:
        return self.fall_speed

    def get_speed_x(self) -> int:
        return self.speed_x