from models.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, speed_x: int = 10, jump_height: int = 10, direction: str = 'none', hp: int = 100,
                 pos: tuple = (50, 0), size: tuple = (50, 50), texture_name: str = 'player_test') -> None:
        super().__init__(speed_x, jump_height, direction, hp, pos, size, texture_name)

        self.__last_move = ''
        self.__is_jump = False
        self.__is_fall = False
        self.__jump_pause = False


    def move(self, keys: tuple, objects: list) -> None:
        nearest = 0

        if (keys[pygame.K_a] and keys[pygame.K_d]) or (not keys[pygame.K_a] and not keys[pygame.K_d]):
            if not self.__is_jump:
                self._stay()

            self.__last_move = ''
            self._move_count = 2 * (self._speed_x != 0)

        elif keys[pygame.K_a]:
            if self.__last_move != 'left':
                self._move_count = 2
                self.__last_move = 'left'
                self._texture_last_move = 'left'

            nearest = -10000
            for obj in objects:
                if obj.is_on_left(self._move_count, self.get_xy(), self.get_size()):
                    if obj.get_x_right() > nearest:
                        nearest = obj.get_x_right()

            if nearest == -10000:
                self._move_left()
            else:
                self._move_left(True, nearest)


        elif keys[pygame.K_d]:
            if self.__last_move != 'right':
                self._move_count = 2 * (self._speed_x != 0)
                self.__last_move = 'right'
                self._texture_last_move = 'right'

            nearest = 10000
            for obj in objects:
                if obj.is_on_right(self._move_count, self.get_xy(), self.get_size()):
                    if obj.get_x_left(self.get_size()) < nearest:
                        nearest = obj.get_x_left(self.get_size())

            if nearest == 10000:
                self._move_right()
            else:
                self._move_right(True, nearest)

        else:
            self.__last_move = ''
            self._texture_last_move = 'right'


        # jumping and falling
        for obj in objects:
            if obj.is_under(self._fall_count, self.get_xy(), self.get_size()):
                self._fall_count = 0

                # jumps
                if not self.__is_jump:
                    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                        self.__is_jump = True
                        self.__jump_pause = True

                    if obj.get_y_up() != self._y:
                        self._fall(True, obj.get_y_up())
                        self.__is_fall = False
                break

            if self.__is_jump:
                if obj.is_upper(self._jump_count, self.get_xy(), self.get_size()):
                    self._jump(True, obj.get_y_down(self.get_size()))
                    self.__is_jump = False
        else:
            if not self.__is_jump:
                self._fall()
                self.__jump_pause = True
                self.__is_fall = True


        # continue jumping
        if self.__is_jump and not self.__jump_pause:
            if not self._jump():
                self.__is_jump = False

        self.__jump_pause = False
        print(nearest)


    def death(self):
        self.tp((100, 0))