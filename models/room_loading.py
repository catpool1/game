from models.player import Player
from models.enemy import Enemy
from models.object import Object
from models.spike import Spike
from models.exit import Exit
from models.lever import Lever
import json


# reading room stats
def room_load(level_name: str) -> tuple:
    with open(f'rooms/{level_name}.json', 'r') as f:
        js = json.load(f)

    player = Player(js['player']['speed_x'], js['player']['fall_speed'], js['player']['jump_height'], js['player']['direction'],
                    js['player']['hp'], js['player']['pos'], js['player']['size'], js['player']['texture_name'])

    enemies = []
    for en in js['enemies']:
        enemies.append(Enemy(en['speed_x'], en['fall_speed'], en['jump_height'], en['direction'],
                             en['hp'], en['pos'], en['size'], en['texture_name']))

    objects = [Object((-10, 0), (10, 900)), Object((1600, 0), (10, 900)),
           Object((0, -10), (2000, 10)), Object((0, 900), (2000, 10))]
    for obj in js['objects']:
        objects.append(Object(obj['pos'], obj['size'], obj['texture']))

    spikes = []
    for sp in js['spikes']:
        spikes.append(Spike(sp['pos'], sp['size'], sp['texture']))

    levers = []
    for lv in js['levers']:
        for obj in objects:
            if obj.get_info()['pos'] == tuple(lv['door_pos']):
                levers.append(Lever(obj, lv['pos'], lv['size'], lv['texture'], lv['switched_texture']))

    exits = []
    for ex in js['exits']:
        exits.append(Exit(ex['pos'], ex['size'], ex['texture'], ex['room_name']))

    backgrounds = []
    for bk in js['backgrounds']:
        backgrounds.append(Object(bk['pos'], bk['size'], bk['texture']))

    return player, enemies, objects, spikes, levers, exits, backgrounds