# Toteuta seuraava luokkahierarkia Python-kielellä:
# Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
# joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.


class Julkaisu:
    def __init__(self, nimi, vuosi):
        self.nimi = nimi
        self.julkaisuvuosi = vuosi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi} ja julkaisuvuosi: {self.julkaisuvuosi}")

# kirjoittaja ja sivumäärä
class Kirja(Julkaisu):
    def __init__(self, nimi, julkaisuvuosi, kirjoittaja, sivumaara):
        super().__init__(nimi, julkaisuvuosi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja} ja sivumäärä: {self.sivumaara}")


#päätoimittaja
class Lehti(Julkaisu):
    def __init__(self, nimi, julkaisuvuosi, paatoimittaja):
        super().__init__(nimi, julkaisuvuosi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")


j = Julkaisu("Magee", 2012)
#print(j.nimi)

k = Kirja("Hytti nro 6.",2000,  "Rosa liksom", 200)
#print(k.nimi)

l = Lehti("Aku Ankka", 1990, "Aki Hyyppä")
#print(l.nimi, "Lehden päätoimittaja on", l.paatoimittaja)

k.tulosta_tiedot()
l.tulosta_tiedot()

