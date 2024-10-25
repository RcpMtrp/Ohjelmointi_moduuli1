import random
class Autotalli:
    def __init__(self):
        self.autot = []
    def auto_sisaan(self, auto):
        # tarkistetaan. ettei auto ole jo tallissa
        # parempi tapa olisi muuttaa lista joukoksi, jolloin duplikaatteja ei sallita
        for a in self.autot:
            if a == auto: # => True jos viittaavat samaan olioon
                return
        self.autot.append(auto)

    def auto_ulos(self, auto):
        self.autot.remove(auto)
        return

    def tulosta_inventaario(self):
        print(f"Autot tallissa:")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()


class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self):
        print(f"Olen {self.nimi}, {self.ika} ja ajan autoa {self.auto.rek_nro}:")
        self.auto.kiihdyta(40)
        print(self.auto.nopeus)
        self.auto.kulje(1)
        self.auto.kiihdyta(140)
        print(self.auto.nopeus)
        self.auto.kulje(0.1)
        self.auto.kiihdyta(-250)
        #print(self.auto.nopeus)
        self.auto.tulosta_ominaisuudet()

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.huippunopeus = huippunopeus
        self.matka = 0
        #self.kuljettaja = "Räikkönen"
        print(f"Auto luoto {rek_nro}, huiput {huippunopeus}km/h")

    def tulosta_rekkari(self):
        print(f"Auton Rekkari: {self.rek_nro}")

    def tulosta_ominaisuudet(self):
        print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.nopeus}, matkamittari: {self.matka}")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        # aika tunneissa
        self.matka += aika * self.nopeus



# Luodaan oliot ja sijoitetaan viittauksen niihin muuttujiin

a1 = Auto("ABC-123", 121)
a2 = Auto("ZYX-789", 250)
kuski = Kuljettaja("Räikkönen", 45, a1)
kuski.aja()
kuski.auto = a2
kuski.aja()

# Luodaan Autotalli-tyyppinen olio ja sijoitetaan autot sinne
talli = Autotalli()
talli.auto_sisaan(a1)
talli.tulosta_inventaario()
talli.auto_sisaan(a2)
#talli.auto_sisaan(a2)
#talli.auto_ulos(a1)

# Luodaan 10 erilaista auto-oliota autotalliin
for i in range(10):
    uusi_auto = Auto(f"ABC-{i + 123}", random.randint(100,200))
    talli.auto_sisaan(uusi_auto)
    #print(Auto)
talli.tulosta_inventaario()

'''
a2.kiihdyta(20)
print(a2.nopeus)
a2.kiihdyta(40)
a1.tulosta_ominaisuudet()
a2.tulosta_ominaisuudet()
'''



#print(f"{a1.rek_nro}, huippunopeus: {a1.huippunopeus}")
#print(f"{a2.rek_nro}, huippunopeus: {a2.huippunopeus}")