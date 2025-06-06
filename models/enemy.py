from models.entity import Entity

class Enemy(Entity):
    def __init__(self, x: int, y: int, width: int, height: int, speed_x: int, hp: int = 100, jump_height: int = 10, texture: str = r'resources\enemy_test.png'):
        super().__init__(x, y, width, height, speed_x, hp, jump_height, texture)

        self.jump_count = self.jump_height
        self.is_jump = False

    def move(self, target_x, target_y):
        if target_x < self.x:
            self.x -= self.speed_x
        elif target_x > self.x:
            self.x += self.speed_x

        if (self.x < target_x) and (self.x + self.speed_x*50 > target_x):
            if target_y != self.y:
                self.is_jump = True

        elif (self.x > target_x) and (self.x - self.speed_x*50 < target_x):
            if target_y != self.y:
                self.is_jump = True

        if self.is_jump:
            if not self.jump():
                self.is_jump = False


    def jump(self):
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