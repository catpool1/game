from models.entity import Entity

class Player(Entity):
    def __init__(self, speed_x: int = 10, fall_speed: int = 6, jump_height: int = 10, hp: int = 100,
                 pos: tuple = (50, 0), size: tuple = (50, 50), texture_name: str = 'player_test') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture_name)

        self.jump_count = jump_height
        self.fall_count = 0
        self.move_count = 2

    def move_right(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            if self.move_count < self.speed_x:
                self.move_count += 1
            self.x += round((self.move_count**1.1) / 2)
        else:
            self.x += distance

    def move_left(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            if self.move_count < self.speed_x:
                self.move_count += 1
            self.x -= round((self.move_count**1.1) / 2)
        else:
            self.x -= distance


    def jump(self, on_distance: bool = False, distance: int = 0) -> bool:
        if not on_distance:
            if self.jump_count >= 0:
                self.y += (self.jump_count ** 2) / 2
                self.jump_count -= 1
            else:
                self.jump_count = self.jump_height
                return False
            return True
        else:
            self.y += distance
            self.jump_count = self.jump_height
            return False

    def fall(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            if self.fall_count < self.fall_speed:
                self.fall_count += 1
            self.y -= (self.fall_count**2) / 2
        else:
            self.y -= distance

    def fall_speed_zeroing(self):
        self.fall_count = 0

    def move_speed_zeroing(self):
        self.move_count = 2

    def get_jump_count(self) -> int:
        return self.jump_count

    def get_fall_count(self) -> int:
        return self.fall_count

    def get_move_count(self) -> int:
        return self.move_count