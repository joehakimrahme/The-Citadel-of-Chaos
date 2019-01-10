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

    def test_random_heros(self):
        heroes = [hero.Hero() for _ in range(1000)]
        self.assertTrue(all(7 <= x.skill <= 12 for x in heroes),
                        "Not all heroes have normal skills")
        self.assertTrue(all(14 <= x.stamina <= 24 for x in heroes),
                        "Not all heroes have normal stamina")
        self.assertTrue(all(7 <= x.luck <= 12 for x in heroes),
                        "Not all heroes have normal luck")

    def test_hero_skill(self):
        test_hero = hero.Hero()
        test_hero.skill += 100
        self.assertTrue(7 <= test_hero.skill <= 12,
                        "hero skill increased beyond initial value")
        test_hero.skill -= 100
        self.assertEqual(test_hero.skill, 0,
                         "hero skill decreased beyond zero")

    def test_hero_stamina(self):
        test_hero = hero.Hero()
        test_hero.stamina += 100
        self.assertTrue(14 <= test_hero.stamina <= 24,
                        "hero stamina increased beyond initial value")
        test_hero.stamina -= 100
        self.assertEqual(test_hero.stamina, 0,
                         "hero skill decreased beyond zero")

    def test_hero_luck(self):
        test_hero = hero.Hero()
        test_hero.luck += 100
        self.assertTrue(7 <= test_hero.luck <= 12,
                        "hero luck increased beyond initial value")
        test_hero.luck -= 100
        self.assertEqual(test_hero.luck, 0,
                         "hero luck decreased beyond zero")
