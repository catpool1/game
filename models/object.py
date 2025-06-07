import pygame
from pygame import SurfaceType


class Object:
    def __init__(self, pos: tuple = (0, 0), size: tuple = (10, 10), texture: str = r'resources\enemy_test.png') -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(texture, (self.width, self.height))

    def blit(self, screen: SurfaceType, screen_height: int) -> None:
        screen.blit(self.texture, (self.x - self.width // 2,
                                 screen_height - self.y - self.height))

    def get_rect(self, screen_height: int) -> tuple:
        return self.x, screen_height - self.y, self.width, self.height