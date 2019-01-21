# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import collections
import unittest

from tcoc import hero


class TestDice(unittest.TestCase):

    def test_simple_dice_roll(self):
        # Simple, every result should be a number in the range [1, 6]
        rolls = [hero.Hero.dice_roll(1) for _ in range(10000)]
        self.assertTrue(all(0 < x <= 6 for x in rolls),
                        "Not all rolls of a single dice return a number "
                        "in the range [1, 6]")

    def test_double_dice_roll(self):
        # As you would surely know if you've ever played The Settlers
        # of Catan, you know that the most common result of a 2-dice
        # roll is 7.
        # (Note): RNG being RNG, this test has failed randomly twice
        rolls_counter = collections.Counter(
            hero.Hero.dice_roll(2) for _ in range(10000))
        most_common = max(rolls_counter, key=lambda x: rolls_counter[x])
        self.assertEqual(most_common,
                         7,
                         "7 is not the most common result for 2-dice rolls")


class TestHero(unittest.TestCase):

    def setUp(self):
        self.test_hero = hero.Hero()
        self.test_hero.magic_random_init()

    def test_random_heros(self):
        heroes = [hero.Hero() for _ in range(1000)]
        self.assertTrue(all(7 <= h.skill <= 12 for h in heroes),
                        "Not all heroes have normal skills")
        self.assertTrue(all(14 <= h.stamina <= 24 for h in heroes),
                        "Not all heroes have normal stamina")
        self.assertTrue(all(7 <= h.luck <= 12 for h in heroes),
                        "Not all heroes have normal luck")

    def test_hero_skill(self):
        _init_value = self.test_hero.skill
        self.test_hero.skill += 100
        self.assertTrue(7 <= self.test_hero.skill <= 12,
                        "hero skill increased beyond initial value")
        self.test_hero.skill -= 100
        self.assertEqual(self.test_hero.skill, 0,
                         "hero skill decreased beyond zero")
        self.test_hero.skill = _init_value

    def test_hero_stamina(self):
        _init_value = self.test_hero.stamina
        self.test_hero.stamina += 100
        self.assertTrue(14 <= self.test_hero.stamina <= 24,
                        "hero stamina increased beyond initial value")
        self.test_hero.stamina -= 100
        self.assertEqual(self.test_hero.stamina, 0,
                         "hero skill decreased beyond zero")
        self.test_hero.stamina = _init_value

    def test_hero_luck(self):
        _init_value = self.test_hero.luck
        self.test_hero.luck += 100
        self.assertTrue(7 <= self.test_hero.luck <= 12,
                        "hero luck increased beyond initial value")
        self.test_hero.luck -= 100
        self.assertEqual(self.test_hero.luck, 0,
                         "hero luck decreased beyond zero")
        self.test_hero.luck = _init_value

    def test_hero_stamina_percentage(self):
        self.test_hero.stamina -= 1
        self.assertTrue(0 < self.test_hero.stamina_percentage < 1,
                        "hero stamina percentage is not a normal "
                        "ratio: %s" % self.test_hero.stamina_percentage)

    def test_random_magic(self):
        spells = sum(self.test_hero.equipped_spells[x] for x in
                     self.test_hero.equipped_spells)

        self.assertEqual(spells, self.test_hero.magic,
                         "hero didn't equip the correct amount of spells")

    def test_random_magic_cast(self):
        start = sum(self.test_hero.equipped_spells[x] for x in
                    self.test_hero.equipped_spells)
        first_spell = next(iter(self.test_hero.equipped_spells))
        self.test_hero.magic_cast(first_spell)
        end = sum(self.test_hero.equipped_spells[x] for x in
                  self.test_hero.equipped_spells)
        self.assertEqual(
            start - end,
            1,
            "cast fail {} {}".format(
                self.test_hero, self.test_hero.equipped_spells))

    def test_quickcombat_win(self):
        _monster = hero.Monster(0, 1)
        win, winner = self.test_hero.quick_combat(_monster)
        self.assertTrue(win, "Lost unlosable quick combat")
        self.assertEqual(winner, self.test_hero, "Wrong winner returned")


class TestMonster(unittest.TestCase):

    def setUp(self):
        self.test_monster = hero.Monster(10, 10)

    def test_monster_stamina_percentage(self):
        self.test_monster.stamina -= 3
        self.assertEqual(self.test_monster.stamina_percentage, 0.7)

    def test_monster_winpercentage(self):
        win, survival, flawless = self.test_monster.winpercentage(10000)
        self.assertTrue(0 <= win <= 1,
                        "Wrong value for wins: {}".format(win))
        self.assertTrue(0 <= survival <= 1,
                        "Wrong value for survival: {}".format(survival))
        self.assertTrue(0 <= flawless <= 1,
                        "Wrong value for survival: {}".format(flawless))

    def test_monster_winpercentage_specific_hero(self):
        test_hero = hero.Hero()
        win, survival, flawless = self.test_monster.winpercentage(
            10000, hero=test_hero)
        self.assertTrue(0 <= win <= 1,
                        "Wrong value for wins: {}".format(win))
        self.assertTrue(0 <= survival <= 1,
                        "Wrong value for survival: {}".format(survival))
        self.assertTrue(0 <= flawless <= 1,
                        "Wrong value for survival: {}".format(flawless))
