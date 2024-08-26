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

gender = input("Mikä on biologinen sukupuolesi?: \n").lower

hemo_value = input("Mikä on hemoglobiiniarvosi?: \n").lower


