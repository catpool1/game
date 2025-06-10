import pygame
from pygame import SurfaceType


class Entity:
    def __init__(self, speed_x: int, fall_speed: int, jump_height: int, hp: int, pos: tuple, size: tuple, texture_name: str) -> None:
        self._x = pos[0]
        self._y = pos[1]
        self._speed_x = speed_x
        self._fall_speed = fall_speed
        self._width = size[0]
        self._height = size[1]
        self._hp = hp
        self._jump_height = jump_height
        self._texture_name = texture_name
        texture = pygame.image.load(f'resources/{texture_name}.png')
        self._texture = pygame.transform.scale(texture, (self._width, self._height))

        self.__jump_count = jump_height
        self.fall_count = 0
        self.move_count = 2


    def blit(self, screen: SurfaceType, screen_height: int) -> None:
        screen.blit(self._texture, (self._x,
                                    screen_height - self._y - self._height))


    def get_xy(self) -> tuple:
        return self._x, self._y

    def get_size(self) -> tuple:
        return self._width, self._height

    def get_rect(self, screen_height: int) -> tuple:
        return self._x, screen_height - self._y, self._width, self._height

    def get_info(self) -> dict:
        return {'_speed_x': self._speed_x, '_fall_speed': self._fall_speed, '_jump_height': self._jump_height,
                '_hp': self._hp, 'pos': (self._x, self._y), 'size': (self._width, self._height), '_texture_name': self._texture_name}


    def is_collided(self, screen_height: int, rect: tuple) -> bool:
        r1 = pygame.Rect(self._x, screen_height - self._y, self._width, self._height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)



    def _move_right(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            if self.move_count < self._speed_x:
                self.move_count += 1
            self._x += round((self.move_count ** 1.1) / 2)
        else:
            self._x += distance

    def _move_left(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            if self.move_count < self._speed_x:
                self.move_count += 1
            self._x -= round((self.move_count ** 1.1) / 2)
        else:
            self._x -= distance


    def _jump(self, on_distance: bool = False, distance: int = 0) -> bool:
        if not on_distance:
            if self.__jump_count >= 0:
                self._y += (self.__jump_count ** 2) / 2
                self.__jump_count -= 1
            else:
                self.__jump_count = self._jump_height
                return False
            return True
        else:
            self._y += distance
            self.__jump_count = self._jump_height
            return False

    def _fall(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            if self.fall_count < self._fall_speed:
                self.fall_count += 1
            self._y -= (self.fall_count ** 2) / 2
        else:
            self._y -= distance