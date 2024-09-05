import random
#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

dice_count = int(input("Valitse arpakuutioiden lukumäärä: "))

roll_amount = [random.randint(1, 6) for _ in range(dice_count)]
for die in range(dice_count):
    dice_roll = random.randint(1, 6)
print(f"{sum(roll_amount)}")

'''
total = 0 
results = []
dice_count = int(input("Valitse arpakuutioiden lukumäärä: "))
for i in range(dice_count):
    result = random.randint(1, 6)
    total = total + result
    results.appent(result)
print(f"noppien silmälukujen summa on {total}")
'''
