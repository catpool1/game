from models.entity import Entity

class Enemy(Entity):
    def __init__(self, speed_x: int = 5, fall_speed: int = 10, jump_height: int = 8, hp: int = 100,
                 pos: tuple = (300, 0), size: tuple = (50, 50), texture: str = r'resources\enemy_test.png') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture)

        self.jump_count = self.jump_height
        self.is_jump = False

    def move(self, target_pos: tuple) -> None:
        target_x, target_y = target_pos[0], target_pos[1]

        if self.x < target_x:
            self.x += self.speed_x

            if self.x + self.speed_x * 50 > target_x:
                if target_y != self.y:
                    self.is_jump = True

        elif self.x > target_x:
            self.x -= self.speed_x

            if self.x - self.speed_x * 50 < target_x:
                if target_y != self.y:
                    self.is_jump = True

        else:
            if target_y != self.y:
                self.is_jump = True

        if self.is_jump:
            if not self.jump():
                self.is_jump = False


    def jump(self) -> bool:
        if self.jump_count >= -self.jump_height:
            if self.jump_count < 0:
                self.y -= (self.jump_count ** 2) / 2
            else:
                self.y += (self.jump_count ** 2) / 2
            self.jump_count -= 1
        else:
            self.jump_count = self.jump_height
            return False
        return True