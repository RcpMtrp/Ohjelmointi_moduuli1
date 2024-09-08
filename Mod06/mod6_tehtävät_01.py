#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

def dice_roll():
    dice_count = random.randint(1, 6)
    return dice_count
    #return random.randint(1, 6)
result = 0
while result != 6:
    result = dice_roll()
    print(result)
#else:
    #print("kutonen" )

#print(dice_roll())
'''
def roll_die():
    return random.randint(1, 6)
'''





