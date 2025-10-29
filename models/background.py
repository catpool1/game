from models.object import Object
import pygame

class Background(Object):
    def __init__(self, pos: tuple = (0, 0), size: tuple = (40, 40), texture: str = 'background 1'):
        super().__init__(pos, size)

        self._texture_name = texture
        self._texture = pygame.transform.scale(pygame.image.load(f'resources/backgrounds/{texture}.png'), (self._width, self._height))