import random

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            # olion omia metodeita kutsuttuaessa käytetään self.
            while kohdekerros > self.kerros:
                self.kerros_ylös()
                if kohdekerros < self.kerros:
                    self.kerros_alas()
        elif kohdekerros < self.kerros:
            while kohdekerros < self.kerros:
                self.kerros_alas()

    def kerros_ylös(self):
        self.kerros += 1
    def kerros_alas(self):
        self.kerros -= 1

class Talo:
    def __init__(self, hissi_lkm, alin_kerros, ylin_kerros):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissi_lkm)]
        self.palohalytin_paalle = False

    def aja_hissia(self, hissin_numero, kohdekerros):
        #if self.palohalytin_paalle:
           # print("Hissit eivät ole toiminnassa")
           # return
        if 0 <= hissin_numero <= len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohdekerros)
            print(f"Hissi {hissin_numero} on kerroksessa {hissi.kerros}")
        else:
            print("Väärä numero")

    def palohalytin(self, fire: bool):
        self.palohalytin_paalle = fire
        if fire != False:
            print("Palohälytin on käynnissä, kaikki hissit menevevät alimpaan kerrokseen.")
            for i, hissi in enumerate(self.hissit):
                hissi.siirry_kerrokseen(0)
                print(f"Hissi {i} kulkee kerrokseen {hissi.kerros}")
        else:
            print("Palohälytin on pysähtynyt, kaikki hissit ovat jälleen toiminnassa.")

talo = Talo(hissi_lkm=3, alin_kerros=0, ylin_kerros=10)

talo.aja_hissia(0, 2)
talo.aja_hissia(1, 4)
talo.aja_hissia(2, 7)
talo.palohalytin(True)
talo.aja_hissia(2, 7)
talo.palohalytin(False)
#talo.aja_hissia(2, 7)
