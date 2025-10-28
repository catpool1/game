from models.object import Object
import pygame

class Lever(Object):
    def __init__(self, door,  pos: tuple = (0, 0), size: tuple = (50, 50), texture: str = 'touch_object_test',
                 switched_texture: str = 'switched_touch_object_test'):
        super().__init__(pos, size, texture)
        self.door = door
        self.switched_texture = switched_texture

    def result(self):
        self.door.tp((-1000, -1000))
        texture = pygame.image.load(f'resources/{self.switched_texture}.png')
        self._texture = pygame.transform.scale(texture, (self._width, self._height))