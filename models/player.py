from models.entity import Entity

class Player(Entity):
    def __init__(self, speed_x: int = 10, fall_speed: int = 7, jump_height: int = 10, hp: int = 100,
                 pos: tuple = (50, 0), size: tuple = (50, 50), texture: str = r'resources\player_test.png') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture)

        self.jump_count = jump_height

    def move_right(self, screen_width: int) -> None:
        if self.x < screen_width - self.width//2:
            if self.x + self.speed_x > screen_width - self.width//2:
                self.x = screen_width - self.width//2
            else:
                self.x += self.speed_x

    def move_left(self) -> None:
        if self.x > self.width//2:
            if self.x - self.speed_x < self.width//2:
                self.x = self.width//2
            else:
                self.x -= self.speed_x

    def jump(self) -> bool:
        if self.jump_count >= 0:
            if self.jump_count > 0:
                self.y += (self.jump_count ** 2) / 2
            self.jump_count -= 1
        else:
            self.jump_count = self.jump_height
            return False
        return True

    def fall(self, distance: int = 0) -> None:
        if not distance:
            self.y -= self.fall_speed
        else:
            self.y -= distance