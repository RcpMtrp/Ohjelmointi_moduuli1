#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.
name_list = set({})

name_input = input("Syötä nimi: ")
#name_list.add(name_input)
while name_input != "":
    if name_input in name_list:
        print("Aiemmin syötetty nimi")
    else:
        name_list.add(name_input)
        print("Uusi nimi")
    name_input = input("Syötä nimi: ")

for name in name_list:
    print(name)
'''
    name_input = input("Syötä nimi: ")
    if name_input != "":
        name_list.add(name_input)
print(name_list)

for i in name_list:
    print(i)
    if i == name_input:
        print("Aiemmin syötetty nimi")
'''

