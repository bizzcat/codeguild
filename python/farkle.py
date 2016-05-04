# IMPORTS / INDICES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
dice_value = {'d1': 0, 'd2': 0, 'd3': 0, 'd4': 0, 'd5': 0}
dice_value_final = {'d1': 0, 'd2': 0, 'd3': 0, 'd4': 0, 'd5': 0}
points = []
omits_left = 4
game_key_for_dice = '\n\nDice One = d1\nDice Two = d2\nDice Three = d3\nDice Four = d4\nDice Five = d5\n'
# DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_dice_value(dice_value):
    print ('\nYour dice values are ' + str(dice_value) + '!\n')

def print_points(points):
    print ('\nYou just scored ' + str(sum(points)) + '!\n')

def print_final_values(dice_value_final):
    print ('\nYour final dice are ' + str(dice_value_final) + '. congratulations!\n')

def print_final_points(points):
    print('\nYour final score is ' + str(sum(points)) + '!!! Congratulations you farkling farkler :)\n\n')

def roll_prompt():
    print ("\nEnter 'Y' to roll your dice!\n")
    roll = input('> ').upper()
    return roll == 'Y'

def roll_again_prompt():
    print ('\nWould you like to change some dice? (Y or N)\n')
    roll = input('> ').upper()
    if roll == 'Y':
        points = [0]
    return roll == 'Y'
    return points

def change_dice_value(dice_value):
    dice_value['d1'] = random.randint(1, 6)
    dice_value['d2'] = random.randint(1, 6)
    dice_value['d3'] = random.randint(1, 6)
    dice_value['d4'] = random.randint(1, 6)
    dice_value['d5'] = random.randint(1, 6)
    return dice_value

def dice_values_to_points(points, dice_value):
    one_count = (list(dice_value.values())).count(1)
    five_count = (list(dice_value.values())).count(5)

    if 1 in (dice_value.values()):
        points.append((100 * one_count))
    if 5 in (dice_value.values()):
        points.append((50 * five_count))
    if (list(dice_value.values())).count(1) == 3:
        points.append(1000)
    if (list(dice_value.values())).count(2) == 3:
        points.append(200)
    if (list(dice_value.values())).count(3) == 3:
        points.append(300)
    if (list(dice_value.values())).count(4) == 3:
        points.append(400)
    if (list(dice_value.values())).count(5) == 3:
        points.append(500)
    if (list(dice_value.values())).count(6) == 3:
        points.append(600)
    return points

def omit_chosen_dice(dice_value, omits_left, dice_value_final):
    print ('\n\n\nWhich dice would you like to roll again?\nMust chose to keep atleast one. You can only re-roll ' + str(omits_left) + ' more dice.\n\n' + str(dice_value) + game_key_for_dice + '\n(Please type with only spaces in between each chosen dice)\n')

    dice_to_omit = (input('> ')).split()
    omits_left = (omits_left - len(dice_to_omit))

    if 'd1' in dice_to_omit:
        dice_value['d1'] = random.randint(1, 6)
    if 'd2' in dice_to_omit:
        dice_value['d2'] = random.randint(1, 6)
    if 'd3' in dice_to_omit:
        dice_value['d3'] = random.randint(1, 6)
    if 'd4' in dice_to_omit:
        dice_value['d4'] = random.randint(1, 6)
    if 'd5' in dice_to_omit:
        dice_value['d5'] = random.randint(1, 6)

    if 'd1' not in dice_to_omit:
        dice_value_final['d1'] = dice_value['d1']
    if 'd2' not in dice_to_omit:
        dice_value_final['d2'] = dice_value['d2']
    if 'd3' not in dice_to_omit:
        dice_value_final['d3'] = dice_value['d3']
    if 'd4' not in dice_to_omit:
        dice_value_final['d4'] = dice_value['d4']
    if 'd5' not in dice_to_omit:
        dice_value_final['d5'] = dice_value['d5']

    if omits_left <= 0:
        print ('Zero choices left! Finishing round!')
        roll = False

    return dice_value
    return omits_left
    return dice_value_final

# CALLING FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print ('Welcome to Farkle! The most farkling ridiculous game on this farkling planet!')

roll = roll_prompt()
while roll:
    dice_value = change_dice_value(dice_value)
    print_dice_value(dice_value)
    points = dice_values_to_points(points, dice_value)
    print_points(points)
    roll = False

dice_value_final['d1'] = dice_value['d1']
dice_value_final['d2'] = dice_value['d2']
dice_value_final['d3'] = dice_value['d3']
dice_value_final['d4'] = dice_value['d4']
dice_value_final['d5'] = dice_value['d5']

roll_again = roll_again_prompt()
while roll_again:
    dice_value = omit_chosen_dice(dice_value, omits_left, dice_value_final)
    print_dice_value(dice_value)
    points = dice_values_to_points(points, dice_value)
    print_points(points)
    dice_values_to_points(points, dice_value)
    roll_again = roll_again_prompt()

cont = True
while cont:
    print_final_values(dice_value_final)
    print_final_points(points)
    cont = False
# FINISH ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

quit()
