from random import randint

class Dice():
    """model a dice"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        x = randint(1, self.sides)

        print(x)

six_sidesDice = Dice(6)
six_sidesDice.roll_dice()

ten_sidedDice = Dice(10)
ten_sidedDice.roll_dice()

twenty_sidedDice = Dice(20)
twenty_sidedDice.roll_dice()