class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = 2000

    def kiihdyta(self, nopeuden_lisa):
        uusi_nopeus = self.nopeus + nopeuden_lisa

        if uusi_nopeus < 0:
            self.nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusi_nopeus

        print(
            f"Auton rekisteritunnus on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus}km/h auton nopeus {auto1.nopeus}, {auto1.matka}")

    def kulje(self, aika):
        ajettu = self.nopeus * aika
        self.matka += ajettu
        print(f"Ajettu matka: {self.matka}")


auto1 = Auto("ABC-123", 142)


auto1.kiihdyta(60)
auto1.kulje(1.5)