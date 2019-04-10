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

print("You find yourself alone in the forest, late at night")
input('press enter to continue')
print("Nothing but the cool night air and darkness surround you")
input('press enter...')
print("You meander through the woods, trying to find any sign of civilization")
input('press enter...')
print('You approach a large, dark structure')
begin = input("Do you enter? (y/n) ")

if begin.lower() == 'n':
    print('An arrow comes flying through the air, piercing your heart')
    input('press enter...')
    print('As you lay on the ground, taking your final breaths, you wish you entered that building')
    exit()
else:
    print('You bravely take your first steps into the structure')

print('You step into a dark room')
input('press enter...')
print('The moodnlight shines in through an old, broken window, illuminating the room')
input('press enter...')
    