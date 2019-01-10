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
