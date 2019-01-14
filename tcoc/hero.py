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
    def stamina_percentage(self):
        return self.stamina / self.initial_stamina

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

    def quick_combat(self, monster, verbose=False):
        while (self.stamina > 0 and monster.stamina > 0):
            #print("HP: {} {}".format(self.stamina, monster.stamina))
            hero_attack = self.dice_roll(2) + self.skill
            monster_attack = self.dice_roll(2) + monster.skill
            #print("Rolls: {} {}".format(hero_attack, monster_attack))
            if (hero_attack > monster_attack):
                monster.stamina -= 2
            elif (hero_attack < monster_attack):
                self.stamina -= 2
        if self.stamina > 0:
            if verbose:
                print(self)
            return (True, self)
        else:
            if verbose:
                print(monster)
            return (False, monster)

    def __repr__(self):
        return "H({}, {}, {}, {})".format(self.skill,
                                          self.stamina,
                                          self.luck,
                                          self.magic)

class Monster(object):

    def __init__(self, skill, stamina):
        self.skill = skill
        self.stamina = stamina
        self.initial_stamina = stamina

    @property
    def stamina_percentage(self):
        return self.stamina / self.initial_stamina

    def winpercentage(self, population=1000, hero=None):
        if hero is None:
            combats = [Hero().quick_combat(self) for _ in range(population)]
        else:
            combats = [hero.quick_combat(self) for _ in range(population)]
        win_percentage = sum(1 for win, h in combats if win) / population
        survival_stamina = [h.stamina_percentage for win, h in combats if win]
        survival_percentage = sum(survival_stamina) / population
        flawless_victory = sum(1 for win, h in combats if win and
                               h.stamina_percentage == 1.0) / population
        return win_percentage, survival_percentage, flawless_victory

    def __repr__(self):
        return "M({}, {})".format(self.skill, self.stamina)

