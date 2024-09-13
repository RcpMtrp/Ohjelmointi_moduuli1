#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kuukaudet = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")
järjestysnumero = int(input("Anna numero (1-12): "))
vuodenaika = kuukaudet[järjestysnumero - 1]
#("Joulukuu", "Tammikuu", "Helmikuu",) ("Maaliskuu", "Huhtikuu", "Toukokuu"), ("Kesäkuu", "Heinäkuu", "Elokuu"), ("Syyskuu", "Lokakuu", "Marraskuu") = kuukaudet
print (f"{järjestysnumero}. kuukauden vuodenaika on {vuodenaika}.")

'''
kuukaudet = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
järjestysnumero = int(input("Anna kuukauden numero (1-12): "))
vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

#Talvi, Kevät, Kesä, Syksy = ("Joulukuu", "Tammikuu", "Helmikuu"), ("Maaliskuu", "Huhtikuu", "Toukokuu"), ("Kesäkuu", "Heinäkuu", "Elokuu"), ("Syyskuu", "Lokakuu", "Marraskuu")
vuodenaika = kuukaudet[järjestysnumero - 1]
Talvi, Kevät, Kesä, Syksy = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
print(f"{järjestysnumero}. vuodenaika on {vuodenaika}. {vuodenajat}")

if järjestysnumero <= 2 or järjestysnumero == 12:

#Talvi, Kevät, Kesä, Syksy = kuukaudet

    print(f"{järjestysnumero}. vuodenaika on {vuodenaika}. {vuodenajat}")
'''
'''
vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
järjestysnumero = int(input("Anna kuukauden numero (1-12): "))
if järjestysnumero < 1:
    print("Virheellinen numero.")
elif järjestysnumero > 3 or 12:
    print(f"{vuodenajat[0]}")
'''
