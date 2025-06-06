from models.entity import Entity

class Player(Entity):
    jump_count = 10

    def __init__(self, x: int, y: int, width: int, height: int, speed_x: int, hp: int = 100, jump_height: int = 10, texture: str = r'resources\player_test.png'):
        super().__init__(x, y, width, height, speed_x, hp, jump_height, texture)

    def move_right(self, screen_width):
        if self.x < screen_width - self.width//2:
            if self.x + self.speed_x > screen_width - self.width//2:
                self.x = screen_width - self.width//2
            else:
                self.x += self.speed_x

    def move_left(self):
        if self.x > self.width//2:
            if self.x - self.speed_x < self.width//2:
                self.x = self.width//2
            else:
                self.x -= self.speed_x

    def jump(self):
        if Player.jump_count >= -self.jump_height:
            if Player.jump_count < 0:
                self.y -= (Player.jump_count ** 2) / 2
            else:
                self.y += (Player.jump_count ** 2) / 2
            Player.jump_count -= 1
        else:
            Player.jump_count = self.jump_height
            return False
        return True