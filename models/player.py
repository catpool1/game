from models.entity import Entity

class Player(Entity):
    def __init__(self, speed_x: int = 10, fall_speed: int = 7, jump_height: int = 10, hp: int = 100,
                 pos: tuple = (50, 0), size: tuple = (50, 50), texture: str = r'resources\player_test.png') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture)

        self.jump_count = jump_height
        self.fall_count = 0

    def move_right(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            self.x += self.speed_x
        else:
            self.x += distance

    def move_left(self, on_distance: bool = False, distance: int = 0) -> None:
        if not on_distance:
            self.x -= self.speed_x
        else:
            self.x -= distance


    def jump(self) -> bool:
        if self.jump_count >= 0:
            self.y += (self.jump_count ** 2) / 2
            self.jump_count -= 1
        else:
            self.jump_count = self.jump_height
            return False
        return True

    def fall(self) -> None:
        self.y -= self.fall_speed
        # if self.fall_count >= -self.fall_speed:
        #     self.y -= (self.fall_count ** 2) / 2
        #     self.jump_count -= 1
        # else:
        #     self.fall_count = 0

    def fall_to_distance(self, distance: int) -> None:
        self.y -= distance