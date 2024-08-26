#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

length = float(input("Kuinka pitkä kuha on senttimetreinä?: "))

kuha = 37 - length

if length > 37:
    print("Kuhasi on sallitun mittainen")

else:
    print(f"Laske kuha takaisin järveen, kuhan sallitusta pyyntimitasta puuttuu {kuha} senttimetriä")




