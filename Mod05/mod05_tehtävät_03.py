#

#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

'''
number = int(input("Anna luku: "))
print(number / number)
if number == 1 / number and number / number == 1:
    print("yes")
else:
    print("no")



num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
'''

def is_prime_number(num):
    #result = True
    # jätetään nolla ja negatiiviset luvut kokokaan testaamatta
    if num < 1:
        return False
    for i in range(2, num):
        #print(i)
        if num % i == 0:
            #result = False
            # jos jaollinen jollain i:n arvolla, palautetaan dalso
            # ja funktion suoritus loppuu siihen
            return False
    # jos funktion suoritus on jatkunut tänne asti, niin palautetaan True
    return True #result

#pääohjelma lukee syötteen ja tulostaa vastauksen
user_input = int(input("Enter a whole number (>0): "))

if is_prime_number(user_input):
    print(f"{user_input} is a prime number")
else:
    print(f"{user_input} is not a prime number")


#testataan funktion toimintaa erilaisilla arvoilla
#print(is_prime_number(4))
#print(is_prime_number(7))







