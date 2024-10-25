class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka


auto1 = Auto("ABC-123", 142)

print( f"Auton rekisteritunnus on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus}km/h auton nopeus {auto1.nopeus}, matka {auto1.matka}")





