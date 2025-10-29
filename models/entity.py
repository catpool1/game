import pygame
from pygame import SurfaceType


class Entity:
    def __init__(self, speed_x: int, fall_speed: int, jump_height: int, direction: str, hp: int, pos: tuple, size: tuple, texture_name: str) -> None:
        self._x = pos[0]
        self._y = pos[1]
        self._speed_x = speed_x
        self._fall_speed = fall_speed
        self._width = size[0]
        self._height = size[1]
        self._hp = hp
        self._jump_height = jump_height
        self._direction = direction
        self._texture_name = texture_name
        texture = pygame.image.load(f'resources/{texture_name}/Idle right/Idle 1.png')
        self._texture = pygame.transform.scale(texture, (self._width, self._height))

        self._jump_count = jump_height
        self._fall_count = 0
        self._move_count = 2 * (self._speed_x != 0)
        self._texture_last_move = 'right' # for correct texture direction


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
        return {'speed_x': self._speed_x, 'fall_speed': self._fall_speed, 'jump_height': self._jump_height, 'direction': self._direction,
                'hp': self._hp, 'pos': (self._x, self._y), 'size': (self._width, self._height), 'texture_name': self._texture_name}


    def is_collided(self, screen_height: int, rect: tuple) -> bool:
        r1 = pygame.Rect(self._x, screen_height - self._y, self._width, self._height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)



    def _stay(self, last_move: str = '') -> None: # texture for staying
        if last_move == 'left':
            self._texture_last_move = 'left'

            self._texture = pygame.transform.scale(
                pygame.image.load(f'resources/{self._texture_name}/Idle left/Idle 1.png'),
                (self._width, self._height))

        elif last_move == 'right':
            self._texture_last_move = 'right'

            self._texture = pygame.transform.scale(
                pygame.image.load(f'resources/{self._texture_name}/Idle right/Idle 1.png'),
                (self._width, self._height))


    def _move_right(self, on_distance: bool = False, distance: int = 0) -> None:
        self._texture = pygame.transform.scale(
            pygame.image.load(f'resources/{self._texture_name}/Run right/Run 1.png'),
            (self._width, self._height)) # texture for moving


        if not on_distance:
            if self._move_count < self._speed_x:
                self._move_count += 1
            self._x += round((self._move_count ** 1.1) / 2)
        else:
            self._x = distance


    def _move_left(self, on_distance: bool = False, distance: int = 0) -> None:
        self._texture = pygame.transform.scale(
            pygame.image.load(f'resources/{self._texture_name}/Run left/Run 1.png'),
            (self._width, self._height)) # texture for moving


        if not on_distance:
            if self._move_count < self._speed_x:
                self._move_count += 1
            self._x -= round((self._move_count ** 1.1) / 2)
        else:
            self._x = distance



    def _jump(self, on_distance: bool = False, distance: int = 0) -> bool:
        if self._texture_last_move == 'left': # texture direction
            self._texture = pygame.transform.scale(
                pygame.image.load(f'resources/{self._texture_name}/Jump left/Jump 2.png'),
                (self._width, self._height))

        elif self._texture_last_move == 'right':
            self._texture = pygame.transform.scale(
                pygame.image.load(f'resources/{self._texture_name}/Jump right/Jump 2.png'),
                (self._width, self._height))


        if not on_distance:
            if self._jump_count >= 0:
                self._y += (self._jump_count ** 2) / 2
                self._jump_count -= 1
            else:
                self._jump_count = self._jump_height
                return False
            return True
        else:
            # print(distance, self._y, self._jump_count, (self._jump_count ** 2) / 2)
            self._y = distance
            self._jump_count = self._jump_height
            return False


    def _fall(self, on_distance: bool = False, distance: int = 0) -> bool:
        if self._texture_last_move == 'left': # texture direction
            self._texture = pygame.transform.scale(
                pygame.image.load(f'resources/{self._texture_name}/Jump left/Jump 3.png'),
                (self._width, self._height))

        elif self._texture_last_move == 'right':
            self._texture = pygame.transform.scale(
                pygame.image.load(f'resources/{self._texture_name}/Jump right/Jump 3.png'),
                (self._width, self._height))


        if not on_distance:
            if self._fall_count < self._fall_speed:
                self._fall_count += 1
            self._y -= (self._fall_count ** 2) / 2
            return True
        else:
            self._y = distance
            return False


    def tp(self, pos: tuple) -> None:
        self._x = pos[0]
        self._y = pos[1]