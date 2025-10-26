from random import randint

from lib.game_data import MONSTER_DATA


class Monster:
    def __init__(self, name, level):
        self.name, self.level = name, level

        # stats
        self.element = MONSTER_DATA[name]['stats']['element']
        self.base_stats = MONSTER_DATA[name]['stats']
        self.health = self.base_stats['max_health'] * self.level
        self.energy = self.base_stats['max_energy'] * self.level
        self.health -= randint(0, 200)
        self.energy -= randint(0, 100)

        # xp
        self.xp = randint(0, 1000)
        self.level_up = self.level * 150

    def get_stat(self, stat):
        return self.base_stats[stat] * self.level