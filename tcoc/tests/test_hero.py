import collections
import unittest

from tcoc import hero


class TestDice(unittest.TestCase):

    def test_simple_dice_roll(self):
        # Simple, every result should be a number in the range [1, 6]
        rolls = [hero.Hero.dice_roll(1) for _ in range(1000)]
        self.assertTrue(all(0 < x <= 6 for x in rolls),
                        "Not all rolls of a single dice return a number "
                        "in the range [1, 6]")

    def test_double_dice_roll(self):
        # As you would surely know if you've ever played The Settlers
        # of Catan, you know that the most common result of a 2-dice
        # roll is 7.
        rolls_counter = collections.Counter(
            hero.Hero.dice_roll(2) for _ in range(1000))
        most_common = max(rolls_counter, key=lambda x: rolls_counter[x])
        self.assertEqual(most_common,
                         7,
                         "7 is not the most commonresult for 2-dice rolls")


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

    def test_random_magic(self):
        self.assertEqual(len(self.test_hero.equipped_spells),
                         self.test_hero.magic,
                         "hero didn't equip the correct amount of spells")
