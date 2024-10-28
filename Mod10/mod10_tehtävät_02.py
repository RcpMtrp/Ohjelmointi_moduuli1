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

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero <= len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohdekerros)
            print(f"Hissi {hissin_numero} on kerroksessa {hissi.kerros}")
        else:
            print("Väärä numero")

talo = Talo(hissi_lkm=3, alin_kerros=0, ylin_kerros=10)

talo.aja_hissia(0, 2)
talo.aja_hissia(1, 4)
talo.aja_hissia(2, 7)
