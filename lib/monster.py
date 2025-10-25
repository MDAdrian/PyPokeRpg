from random import randint

from lib.game_data import MONSTER_DATA


class Monster:
    def __init__(self, name, level):
        self.name, self.level = name, level

        # stats
        self.element = MONSTER_DATA[name]['stats']['element']
        self.base_stats = MONSTER_DATA[name]['stats']

        # xp
        self.xp = randint(0, 1000)
        self.level_up = self.level * 150