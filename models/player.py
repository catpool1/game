from models.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, speed_x: int = 10, fall_speed: int = 6, jump_height: int = 10, hp: int = 100,
                 pos: tuple = (50, 0), size: tuple = (50, 50), texture_name: str = 'player_test') -> None:
        super().__init__(speed_x, fall_speed, jump_height, hp, pos, size, texture_name)

        self.last_move = ''
        self.is_jump = False
        self.jump_pause = False


    def move(self, screen_height: int, keys: tuple, objects: list) -> None:
        if keys[pygame.K_a] and keys[pygame.K_d]:
            self.last_move = ''
            self.move_count = 2

        elif keys[pygame.K_a]:
            if self.last_move != 'left':
                self.move_count = 2
                self.last_move = 'left'

            for obj in objects:
                if obj.is_on_left(self.move_count, (self.x, self.y), (self.width, self.height)):
                    self.move_left(True, obj.get_distance_left((self.x, self.y)))
                    break
            else:
                self.move_left()

        elif keys[pygame.K_d]:
            if self.last_move != 'right':
                self.move_count = 2
                self.last_move = 'right'

            for obj in objects:
                if obj.is_on_right(self.move_count, (self.x, self.y), (self.width, self.height)):
                    self.move_right(True, obj.get_distance_right((self.x, self.y), (self.width, self.height)))
                    break
            else:
                self.move_right()

        else:
            self.last_move = ''


        for obj in objects:
            if obj.is_under(screen_height, self.fall_count, (self.x, self.y), (self.width, self.height)):
                self.fall_count = 0

                # jumps
                if not self.is_jump:
                    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                        self.is_jump = True
                        self.jump_pause = True

                    self.fall(True, obj.get_distance_up((self.x, self.y)))
                break

            if self.is_jump:
                if obj.is_upper(screen_height, self.jump_count, (self.x, self.y), (self.width, self.height)):
                    self.jump(True, obj.get_distance_down((self.x, self.y), (self.width, self.height)))
                    self.is_jump = False
        else:
            if not self.is_jump:
                self.fall()
                self.jump_pause = True

        # continue jumping
        if self.is_jump and not self.jump_pause:
            if not self.jump():
                self.is_jump = False

        self.jump_pause = False