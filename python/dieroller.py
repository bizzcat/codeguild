#ask user how many 6 sided dies:
#Roll and print value of each die
#print average of all dies

import random

num_rolls = 0
num_dice = int(input('how many die: '))
sum_dice= 0

while num_rolls < num_dice:
    dice_roll = random.randint(1, 6)
    print ("roll value:", dice_roll)
    sum_dice += dice_roll
    num_rolls += 1

print('the die sum =', sum_dice, "the average =", sum_dice / num_dice)
