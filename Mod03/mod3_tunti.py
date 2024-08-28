from random import random

import random

'''
rahat = float(input("anna rahamäärä:"))
if rahat >= 5:
    print("Voit ostaa latten.")
else:
    print("Et voi ostaa lattea")


# Luo ohjelma joka pyytää käyttäjän numeron ja tulostaa onko: luku pos, neg, vai nolla

Numero = int(input("Anna luku: "))

if Numero > 0:
    print("Numero on positiivinen")
elif Numero < 0:
    print("Numero on negatiivinen")
else:
    print("Numero on 0")
    



user_input = input("Valitse a, b tai c:")
if user_input == "a":
    print("Tehdään jotain, käyttäjä valitsi kirjaimen a")
elif user_input == "b":
    print("Käyttäjä valitsi b")
elif user_input == "c":
    print("Käyttäjä valitsi c")
else:
    print("Käyttäjä ei syöttänyt a, b tai c kirjainta")

print("Ohjelma loppuu")




age = 5
name = "Matti"

print(age < 10 and name == "Matti")

print(age < 10 and name == "Ulla")

print(age < 10 or name == "Ulla")



print(not True)
print(True and True)
print(True and False)
print(True or True)
print(True and (False or True))

result = (False or False) and (False or True)

print(f"Vertailun tulos: {result}")

print(1 < 2 or (1 == 1 and result))

'''
x = 2
while x < 1000:
    print(x)
    x *= 2

'''

#While silmukat (loopit)
# ikuinen loppi, ei hyvä
'''
#while True: 
    #print("Moro")
    #print("Matti!")

max_count = int(input("Kuinka monta kertaa kukutaan? "))

counter = 0

while counter < max_count:
    counter = counter + 1 #lyhyt versio: counter += 1
    print(f"{counter}. kerran Kukkuu")
print(f"Laskurin arvo lopuksi: {counter}")
'''

'''
# noppasimulaattori
# mikä on kahden yhtäaikaisen kutosen todennäköisyys?
round = 100
round_counter = 0
total_rolls = 0
while round_counter < round:
    round_counter += 1
    die1 = 0
    die2 = 0
    roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        #print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}")
    #print(f"Noppaa heitettiin {roll_counter} kertaa.")
    total_rolls = total_rolls + roll_counter
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / round} heitolla")
'''
# ohjelma komentorivikäyttöliittymä
command = ""

while command != "lopeta":
    command = input("Komento, kiitos> ")
    if command == "lopeta":
        print("Lopetetaan.")
        #break # "heittää ulos"  loopista, ei paras ohjelmointikäytäntö
    elif command == "kukkuu":
        max_count = int(input("Kuinka monta kertaa kukutaan? "))
        counter = 0
        while counter < max_count:
            counter = counter + 1
            print(f"{counter}. kerran Kukkuu")
        print(f"Laskurin arvo lopuksi: {counter}")
    elif command == "noppa":
        round = 100
        round_counter = 0
        total_rolls = 0
        while round_counter < round:
            round_counter += 1
            die1 = die 2 = roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
            total_rolls = total_rolls + roll_counter
        print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / round} heitolla")

    else:
        print("En ymmärrä komentoa. Yritä uudestaan, kiitos.")

print("Ohjelma sammutettu.")
