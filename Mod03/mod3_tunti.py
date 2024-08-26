

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

'''


age = 5
name = "Matti"

print(age < 10 and name == "Matti")

print(age < 10 and name == "Ulla")

print(age < 10 or name == "Ulla")




