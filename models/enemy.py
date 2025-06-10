from models.entity import Entity

class Enemy(Entity):
    def __init__(self, speed_x: int = 5, fall_speed: int = 10, jump_height: int = 8, hp: int = 100,
                 pos: tuple = (300, 0), size: tuple = (50, 50), texture_name: str = 'enemy_test') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture_name)

        self.__jump_count = self._jump_height
        self.__is_jump = False

    def move(self, target_pos: tuple) -> None:
        target_x, target_y = target_pos[0], target_pos[1]

        if self._x < target_x:
            self._x += self._speed_x

            if self._x + self._speed_x * 50 > target_x:
                if target_y != self._y:
                    self.__is_jump = True

        elif self._x > target_x:
            self._x -= self._speed_x

            if self._x - self._speed_x * 50 < target_x:
                if target_y != self._y:
                    self.__is_jump = True

        else:
            if target_y != self._y:
                self.__is_jump = True

        if self.__is_jump:
            if not self._jump():
                self.__is_jump = False