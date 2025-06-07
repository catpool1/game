import pygame
from pygame import SurfaceType


class Object:
    def __init__(self, pos: tuple = (0, 0), size: tuple = (10, 10), texture: str = r'resources\enemy_test.png') -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(texture, (self.width, self.height))

    def blit(self, screen: SurfaceType, screen_height: int) -> None:
        screen.blit(self.texture, (self.x - self.width // 2,
                                 screen_height - self.y - self.height))

    def get_rect(self, screen_height: int) -> tuple:
        return self.x, screen_height - self.y, self.width, self.height

    def is_collided_up(self, screen_height: int, target_pos: tuple, target_size: tuple) -> bool:
        target_x, target_y = target_pos[0], target_pos[1]
        target_width, target_height = target_size[0], target_size[1]

        if (self.x + self.width >= target_x >= self.x) or (self.x <= target_x + target_width <= self.x + self.width):
            if screen_height - target_y == screen_height - self.y - self.height:
                return True
        return False

    def is_under(self, screen_height: int, target_fall_speed: int, target_pos: tuple, target_size: tuple) -> bool:
        target_x, target_y = target_pos[0], target_pos[1]
        target_width, target_height = target_size[0], target_size[1]

        if (self.x + self.width >= target_x >= self.x) or (self.x <= target_x + target_width <= self.x + self.width):
            if screen_height - target_y < screen_height - self.y - self.height:
                if screen_height - target_y + target_fall_speed >= screen_height - self.y - self.height:
                    return True
        return False

    def get_distance(self, target_pos: tuple) -> int:
        target_y = target_pos[1]
        return target_y - (self.y + self.height)