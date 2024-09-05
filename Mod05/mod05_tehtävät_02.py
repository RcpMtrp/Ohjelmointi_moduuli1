#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
#lajittelujärjestyksen voi kääntää antamalla sort-metodille
#argumentiksi reverse=True.

number_list = []
#max_num = min_num = number_list
numbers = input("Anna luku tai lopeta painamalla Enter: ")
#print(numbers)

while numbers != "":
    number_list.append(int(numbers))
    numbers = input("Anna seuraava luku tai lopeta painamalla Enter: ")
print(number_list)
sorted_list = sorted(number_list, reverse=True)
#number_list.sort(reverse=True)
print(sorted_list)


numbers = [5, 2, 6, 8, 1]
sort_num = sorted(numbers, reverse=True)
print(sort_num)


