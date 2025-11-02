from models.object import Object

class Spike(Object):
    def __init__(self, pos: tuple = (0, 0), size: tuple = (40, 40), texture: str = 'enemy_test'):
        super().__init__(pos, size, texture)

    @staticmethod
    def result(player) -> None:
        player.death()