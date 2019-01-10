import random


class Hero(object):

    spells = (
        "Creature Copy",
        "E.S.P.",
        "Fire",
        "Fool's Gold",
        "Illusion",
        "Levitation",
        "Luck",
        "Shielding",
        "Skill",
        "Stamina",
        "Strength",
        "Weakness",
    )

    # This method can probably be moved to a separate module later
    @staticmethod
    def dice_roll(dice_count=1):
        return sum(random.randint(1, 6) for _ in range(dice_count))

    def __init__(self, skill=None, stamina=None, luck=None, magic=None):
        # provide random defaults if no values are provided
        self._attributes = {
            "skill": skill,
            "stamina": stamina,
            "luck": luck,
            "magic": magic
        }
        # explicitly initalize properties to make sure we get valid
        # values
        if self._attributes["skill"] is None:
            self._attributes["skill"] = self.dice_roll(1) + 6
            self.initial_skill = self._attributes["skill"]
        if self._attributes["stamina"] is None:
            self._attributes["stamina"] = self.dice_roll(2) + 12
            self.initial_stamina = self._attributes["stamina"]
        if self._attributes["luck"] is None:
            self._attributes["luck"] = self.dice_roll(1) + 6
            self.initial_luck = self._attributes["luck"]
        self.equipped_spells = []
        self.gold = 0
        self.equipment = ['sword', 'leather armor', 'lantern', 'backpack']

    @property
    def skill(self):
        return self._attributes["skill"]

    @skill.getter
    def skill(self):
        return self._attributes["skill"]

    @skill.setter
    def skill(self, value):
        print(value, self.initial_skill)
        switch = {
            True: value,
            value > self.initial_skill: self.initial_skill,
            value < 0: 0,
        }
        print(switch)
        self._attributes["skill"] = switch[True]

    @property
    def stamina(self):
        return self._attributes["stamina"]

    @stamina.getter
    def stamina(self):
        return self._attributes["stamina"]

    @stamina.setter
    def stamina(self, value):
        switch = {
            True: value,
            value > self.initial_stamina: self.initial_stamina,
            value < 0: 0,
        }
        self._attributes["stamina"] = switch[True]

    @property
    def luck(self):
        return self._attributes["luck"]

    @luck.getter
    def luck(self):
        return self._attributes["luck"]

    @luck.setter
    def luck(self, value):
        switch = {
            True: value,
            value > self.initial_luck: self.initial_luck,
            value < 0: 0,
        }
        self._attributes["luck"] = switch[True]

    @property
    def magic(self):
        return self._attributes["magic"]

    @magic.getter
    def magic(self):
        if self._attributes["magic"] is None:
            self._attributes["magic"] = self.dice_roll(2) + 6
        return self._attributes["magic"]

    def magic_random_init(self):
        for _ in range(self.magic):
            self.equipped_spells.append(random.choice(Hero.spells))
