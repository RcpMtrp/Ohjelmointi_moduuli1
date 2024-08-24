import math
import random
#1.

age = input("kerro nimesi \n")

print("Hei " + age + "!")

#2. Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#pii*r^2



r = float(input("Anna ympyrän säde (m): "))

area = math.pi * r * r

print(f"Ympyrän, jonka säde on {r}, pinta-ala on {area:.1f} neliömetriä.")


#satunnaisen kokonaisluvun arpominen väliltä 1-6
#random_number = random.randint(1, 6)
#print(f"Satunnainen luku 1-6: {random_number}")

# 3.Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("Anna suorakulmion kanta (m): "))

korkeus = float(input("Anna suorakulmion korkeus (m): "))

pinta_ala = kanta * korkeus
piiri = kanta + kanta + korkeus + korkeus
print(f"Suorakulmion, jonka kanta on {kanta} ja korkeus {korkeus}, pinta-ala on {pinta_ala:.1f} neliömetriä ja piiri {piiri:.1f} metriä.")

#4. Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

a = float(input("Anna luku a:"))
b = float(input("Anna luku b:"))
c = float(input("Anna luku c:"))

summa = a + b + c
tulo = a * b * c
keskiarvo = tulo / 3

print(f"summa {summa}, tulo {tulo}, keskiarvo {keskiarvo}")


# 5.Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#
#     Yksi leiviskä on 20 naulaa.   leiviska = 20 * naula
#     Yksi naula on 32 luotia.      naula = 32 * luoti
#     Yksi luoti on 13,3 grammaa.   luoti = 13.5
# Anna leiviskät.
# 3
# Anna naulat.
# 9
# Anna luodit.
# 13.5
# Massa nykymittojen mukaan:
# 29 kilogrammaa ja 545.95 grammaa.

leiviska = float(input("Anna leiviskät: "))

naula = float(input("Anna naulat: "))

luoti = float(input("Anna luodit: "))

naula_conv = leiviska * 20

luoti_conv = (naula_conv + naula) * 32

tulos = (luoti_conv + luoti) * 13.5

tulos_string = str(tulos)

print("Massa nykymittojen mukaan: \n" + tulos_string[0:2] + " kilogrammaa ja " + tulos_string[2:8] + " grammaa.")


#6.

first_number = str(random.randint(0,9))
second_number = str(random.randint(0,9))
third_number = str(random.randint(0,9))
#_number
fourth_number = str(random.randint(1,6))
fifth_number = str(random.randint(1,6))
sixth_number = str(random.randint(1,6))
digits_first = first_number + second_number + third_number
digits_second = fourth_number + fifth_number + sixth_number
print("Your three digit code: " + digits_first + " and four digit code: " + digits_second)



