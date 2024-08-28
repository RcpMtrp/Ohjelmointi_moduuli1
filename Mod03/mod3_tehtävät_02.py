'''

#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla
# olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
    LUX on parvekkeellinen hytti yläkannella.
    A on ikkunallinen hytti autokannen yläpuolella.
    B on ikkunaton hytti autokannen yläpuolella.
    C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.



hytti = input ("Mikä on hyttlikuokkasi? LUX, A, B tai C \n").lower

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")
'''


#

#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#   Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = input("Mikä on biologinen sukupuolesi?: \n")

#hemo_value = input("Mikä on hemoglobiiniarvosi?: \n")

if gender == "mies":
  hemo_value = float(input("mMikä on hemoglobiiniarvosi?: "))
if 134 <= hemo_value <= 195:
  print("Hemoglobiini arvosi on normaali.")
elif hemo_value > 195:
  print("Hemoglobiini arvosi on korkea.")
else:
  print("Hemoglobiini arvosi on matala.")
ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
  paino = float(input("Anna paino (kg): "))
if (ikä >= 18 or ikä >= 15 and paino >= 55):
  print("Lääkkeen käyttö on sallittua.")


'''
def CheckLeap(Year):

  if(Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0):
    print("Tämä on karkausvuosi")

  else:
    print ("Tämä ei ole karkausvuosi")

Year = int(input("Anna vuosiluku"))

CheckLeap(Year)
'''