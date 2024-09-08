#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.





def lukujensumma():
    number_list = []
    numbers = input("Anna kokonaislukuja ja paina enter lopettaaksesi.")
    while numbers != "":
        number_list.append(int(numbers))
        numbers = input("Anna seuraava luku tai lopeta painamalla Enter: ")
    summed_list = sum(number_list)
    return summed_list
    #print(summed_list)

tulos = lukujensumma()
print(tulos)
'''

def lukujensumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
tulos = lukujensumma(luku1, luku2)
print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}.")


'''
