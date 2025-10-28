from models.object import Object
import pygame

class Exit(Object):
    def __init__(self, pos: tuple = (0, 0), size: tuple = (50, 50), texture: str = 'exit_test', room_name: str = 'test'):
        super().__init__(pos, size, texture)
        self.room_name = room_name

    def room(self):
        return self.room_name