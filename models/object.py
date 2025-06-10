import pygame
from pygame import SurfaceType


class Object:
    def __init__(self, pos: tuple = (0, 0), size: tuple = (10, 10), texture: str = 'object_standard') -> None:
        self._x = pos[0]
        self._y = pos[1]
        self._width = size[0]
        self._height = size[1]
        self._texture_name = texture
        texture = pygame.image.load(f'resources/{texture}.png')
        self._texture = pygame.transform.scale(texture, (self._width, self._height))


    def blit(self, screen: SurfaceType, screen_height: int) -> None:
        screen.blit(self._texture, (self._x,
                                    screen_height - self._y - self._height))

    def get_rect(self, screen_height: int) -> tuple:
        return self._x, screen_height - self._y, self._width, self._height

    def get_info(self) -> dict:
        return {'pos': (self._x, self._y), 'size': (self._width, self._height), '_texture': self._texture_name}


    def is_under(self, screen_height: int, target_fall_count: int, target_pos: tuple, target_size: tuple) -> bool:
        target_x, target_y = target_pos[0], target_pos[1]
        target_width, target_height = target_size[0], target_size[1]

        if (self._x + self._width > target_x > self._x) or (self._x < target_x + target_width < self._x + self._width):
            if screen_height - target_y <= screen_height - self._y - self._height:
                if screen_height - target_y + (target_fall_count**2)/2 >= screen_height - self._y - self._height:
                    return True
        return False

    def get_distance_up(self, target_pos: tuple) -> int:
        target_y = target_pos[1]
        return target_y - (self._y + self._height)


    def is_on_right(self, target_move_count: int, target_pos: tuple, target_size: tuple) -> bool:
        target_x, target_y = target_pos[0], target_pos[1]
        target_width, target_height = target_size[0], target_size[1]

        if not ((target_y >= self._y + self._height) or (target_y + target_height <= self._y)):
            if target_x + target_width <= self._x:
                if target_x + target_width + round((target_move_count**1.1) / 2) > self._x - 1:
                    return True
        return False

    def get_distance_right(self, target_pos: tuple, target_size: tuple) -> int:
        target_x = target_pos[0]
        target_width = target_size[0]
        return self._x - target_x - target_width


    def is_on_left(self, target_move_count: int, target_pos: tuple, target_size: tuple) -> bool:
        target_x, target_y = target_pos[0], target_pos[1]
        target_width, target_height = target_size[0], target_size[1]

        if not ((target_y >= self._y + self._height) or (target_y + target_height <= self._y)):
            if target_x >= self._x + self._width:
                if target_x - round((target_move_count**1.1) / 2) <= self._x + self._width + 1:
                    return True
        return False

    def get_distance_left(self, target_pos: tuple) -> int:
        target_x = target_pos[0]
        return target_x - (self._x + self._width)


    def is_upper(self, screen_height: int, target_jump_count: int, target_pos: tuple, target_size: tuple) -> bool:
        target_x, target_y = target_pos[0], target_pos[1]
        target_width, target_height = target_size[0], target_size[1]

        if (self._x + self._width > target_x > self._x) or (self._x < target_x + target_width < self._x + self._width):
            if screen_height - target_y >= screen_height - self._y - self._height:
                if screen_height - target_y - target_height - (target_jump_count**2)/2 <= screen_height - self._y:
                    return True
        return False

    def get_distance_down(self, target_pos: tuple, target_size: tuple) -> int:
        target_y = target_pos[1]
        target_height = target_size[1]
        return self._y - target_y - target_height
