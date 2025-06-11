from models.entity import Entity

class Enemy(Entity):
    def __init__(self, speed_x: int = 5, fall_speed: int = 10, jump_height: int = 8, direction: str = 'right', hp: int = 100,
                 pos: tuple = (300, 0), size: tuple = (50, 50), texture_name: str = 'enemy_test') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture_name)

        self.__last_move = ''
        self.__direction = direction

    def move(self, screen_height: int, objects: list) -> None:

        if self.__direction == 'left':
            if self.__last_move != 'left':
                self._move_count = 2 * (self._speed_x != 0)
                self.__last_move = 'left'

            for obj in objects:
                if obj.is_on_left(self._move_count, (self._x, self._y), (self._width, self._height)):
                    self._move_left(True, obj.get_distance_left((self._x, self._y)))
                    self.__direction = 'right'
                    break

                if obj.is_on_left_edge(self._move_count, (self._x, self._y)):
                    self._move_left(True, obj.get_distance_right((self._x - self._width, self._y), (self._width, self._height)))
                    self.__direction = 'right'
                    break
            else:
                self._move_left()

        elif self.__direction == 'right':
            if self.__last_move != 'right':
                self._move_count = 2 * (self._speed_x != 0)
                self.__last_move = 'right'

            for obj in objects:
                if obj.is_on_right(self._move_count, (self._x, self._y), (self._width, self._height)):
                    self._move_right(True, obj.get_distance_right((self._x, self._y), (self._width, self._height)))
                    self.__direction = 'left'
                    break

                if obj.is_on_right_edge(self._move_count, (self._x, self._y), (self._width, self._height)):
                    self._move_right(True, obj.get_distance_left((self._x + self._width, self._y)) * (self._speed_x != 0))
                    self.__direction = 'left'
                    break
            else:
                self._move_right()

        else:
            self.__last_move = ''


        for obj in objects:
            if obj.is_under(screen_height, self._fall_count, (self._x, self._y), (self._width, self._height)):
                self._fall_count = 0
                self._fall(True, obj.get_distance_up((self._x, self._y)))
                break
        else:
            self._fall()