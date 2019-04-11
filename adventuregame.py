# This is a basic text-based adventure game
# Created by Dallin Reeves
# April 9, 2019 12:35PM

import random

min = 1
max = 6
something = "something in the shadows that I can't see"

inventory = []
rm1 = ['dice', 'axe', 'knife', 'artifact', 'gas can']
leftrm = ['painting', 'spiderweb', 'torch']
rightrm = ['skeleton', 'lighter']
forwardrm = [something]

print("\nYou find yourself alone in the forest, late at night")
input('press enter to continue')
print("\nNothing but the cool night air and darkness surround you")
input('press enter...')
print("\nYou meander through the woods, trying to find any sign of civilization")
input('press enter...')
print('\nYou approach a large, dark structure')
begin = input("Do you enter? (y/n) ")

if begin.lower() == 'n':
    print('\nAn arrow comes flying through the air, piercing your heart')
    input('press enter...')
    print('\nAs you lay on the ground, taking your final breaths, you wish you entered that building')
    exit()
else:
    print('\nYou bravely take your first steps into the structure')
    input('press enter...')

print('\nYou step into a dark room')
input('press enter...')
print('\nThe moonlight shines in through an old, broken window, illuminating the room')
input('press enter...')
print('\nYou notice 3 doors: straight ahead, to the left, and to the right')
input('press enter...')
print('\nYou also notice several items scattered throughout the room')
action1 = input('\nDo you want to look around the room, \nor go to one of the other rooms (look, right, left, or straight)? ')

if action1.lower() == 'look':
    print('\nYou take a closer look at the items on the floor')
    input('press enter...')
    print('\nLeaning against the wall, covered in dust, you find an ' + rm1[1])
    input('press enter...')