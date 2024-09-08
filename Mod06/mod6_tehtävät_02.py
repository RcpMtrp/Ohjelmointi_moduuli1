import random
user_input = int(input("Anna tahkojen lukumäärä: "))
def dice_roll(user_input):
    dice_count = random.randint(1, user_input)
    return dice_count
    #return random.randint(1, 6)
result = 0
while result != user_input:
    result = dice_roll(user_input)
    print(result)
