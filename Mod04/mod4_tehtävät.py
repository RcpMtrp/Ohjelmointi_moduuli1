import random
#Kirjoita while-toistorakennetta
# käyttävä ohjelma, joka tulostaa kolmella jaolliset
# luvut väliltä 1..1000

'''

counter = 0

while counter < 1000:
    counter = counter + 3 #lyhyt versio: counter += 1
    print(f"{counter - 2}.")
'''
'''
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuuman lukumäärä: "))

cm = tuuma * 2.54

while tuuma >= 0:
    print(f"{cm}")
    tuuma = float(input("Anna tuuman lukumäärä: "))
    cm = tuuma * 2.54
print("Ohjelma lopetettu")

Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

'''
'''
player_guess = float(input("Arvaa koneen arpoma luku: "))

random_number = random.randint(1, 10)
while player_guess != random_number:
    if player_guess > random_number:
        print("Arvauksesi on liian korkea.")
    elif player_guess < random_number:
        print("Arvauksesi on liian alhainen.")
    player_guess = float(input("Arvaa koneen arpoma luku: "))

print("Arvasit oikein.")
'''
'''
round = 100
round_counter = 0total_rolls = 0
while round_counter < round:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        #print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}")
    #print(f"Noppaa heitettiin {roll_counter} kertaa.")
    total_rolls = total_rolls + roll_counter
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / round} heitolla")

'''
'''
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).
'''
username = "python"
password = "salasana"
login = input("Anna käyttäjätunnus: ")
password = "salasana"
if login == "python":
    input("Anna salasana: ")
while login != "python" and password != "salasana":
    print("Pääsy evätty.")



print("Tervetuloa.")



