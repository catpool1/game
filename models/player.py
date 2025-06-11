from models.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, speed_x: int = 10, fall_speed: int = 6, jump_height: int = 10, hp: int = 100,
                 pos: tuple = (50, 0), size: tuple = (50, 50), texture_name: str = 'player_test') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture_name)

        self.__last_move = ''
        self.__is_jump = False
        self.__jump_pause = False


    def move(self, screen_height: int, keys: tuple, objects: list) -> None:
        if keys[pygame.K_a] and keys[pygame.K_d]:
            self.__last_move = ''
            self._move_count = 2 * (self._speed_x != 0)

        elif keys[pygame.K_a]:
            if self.__last_move != 'left':
                self._move_count = 2
                self.__last_move = 'left'

            for obj in objects:
                if obj.is_on_left(self._move_count, (self._x, self._y), (self._width, self._height)):
                    self._move_left(True, obj.get_distance_left((self._x, self._y)))
                    break
            else:
                self._move_left()

        elif keys[pygame.K_d]:
            if self.__last_move != 'right':
                self._move_count = 2 * (self._speed_x != 0)
                self.__last_move = 'right'

            for obj in objects:
                if obj.is_on_right(self._move_count, (self._x, self._y), (self._width, self._height)):
                    self._move_right(True, obj.get_distance_right((self._x, self._y), (self._width, self._height)))
                    break
            else:
                self._move_right()

        else:
            self.__last_move = ''


        for obj in objects:
            if obj.is_under(screen_height, self._fall_count, (self._x, self._y), (self._width, self._height)):
                self._fall_count = 0

                # jumps
                if not self.__is_jump:
                    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                        self.__is_jump = True
                        self.__jump_pause = True

                    self._fall(True, obj.get_distance_up((self._x, self._y)))
                break

            if self.__is_jump:
                if obj.is_upper(screen_height, self._jump_count, (self._x, self._y), (self._width, self._height)):
                    self._jump(True, obj.get_distance_down((self._x, self._y), (self._width, self._height)))
                    self.__is_jump = False
        else:
            if not self.__is_jump:
                self._fall()
                self.__jump_pause = True

        # continue jumping
        if self.__is_jump and not self.__jump_pause:
            if not self._jump():
                self.__is_jump = False

        self.__jump_pause = False