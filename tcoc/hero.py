import random


class Hero(object):

    # This method can probably be moved to a separate module later
    @staticmethod
    def dice_roll(dice_count=1):
        return sum(random.randint(1, 6) for _ in range(dice_count))
