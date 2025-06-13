from models.object import Object
import pygame

class Spike(Object):
    def __init__(self, pos: tuple = (0, 0), size: tuple = (40, 40), texture: str = 'object_standard'):
        super().__init__(pos, size, texture)

    def is_collided(self, screen_height: int, rect: tuple) -> bool:
        r1 = pygame.Rect(self._x, screen_height - self._y, self._width, self._height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)