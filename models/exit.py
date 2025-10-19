from models.object import Object
import pygame

class Exit(Object):
    def __init__(self, pos: tuple = (0, 0), size: tuple = (50, 50), texture: str = 'exit_test'):
        super().__init__(pos, size, texture)

    def is_collided(self, screen_height: int, rect: tuple) -> bool:
        r1 = pygame.Rect(self._x, screen_height - self._y, self._width, self._height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)

    @staticmethod
    def result(player):
        player.tp((100, 500))