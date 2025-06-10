import pygame
from pygame import SurfaceType


class Entity:
    def __init__(self, speed_x: int, fall_speed: int, jump_height: int, hp: int, pos: tuple, size: tuple, texture_name: str) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.speed_x = speed_x
        self.fall_speed = fall_speed
        self.width = size[0]
        self.height = size[1]
        self.hp = hp
        self.jump_height = jump_height
        self.texture_name = texture_name
        texture = pygame.image.load(f'resources/{texture_name}.png')
        self.texture = pygame.transform.scale(texture, (self.width, self.height))

        self.jump_count = jump_height
        self.fall_count = 0
        self.move_count = 2


    def blit(self, screen: SurfaceType, screen_height: int) -> None:
        screen.blit(self.texture, (self.x,
                                 screen_height - self.y - self.height))


    def get_xy(self) -> tuple:
        return self.x, self.y

    def get_size(self) -> tuple:
        return self.width, self.height

    def get_rect(self, screen_height: int) -> tuple:
        return self.x, screen_height - self.y, self.width, self.height

    def get_info(self) -> dict:
        return {'speed_x': self.speed_x, 'fall_speed': self.fall_speed, 'jump_height': self.jump_height,
                'hp': self.hp, 'pos': (self.x, self.y), 'size': (self.width, self.height), 'texture_name': self.texture_name}


    def is_collided(self, screen_height: int, rect: tuple) -> bool:
        r1 = pygame.Rect(self.x, screen_height - self.y, self.width, self.height)
        r2 = pygame.Rect(rect)
        return r1.colliderect(r2)



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