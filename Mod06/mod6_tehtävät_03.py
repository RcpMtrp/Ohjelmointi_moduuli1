#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.
'''
user_input = float(input("Give fuel amount to convert: "))
def gallon_converter(fuel):
    while user_input > 0:
        #print(user_input)
        #litre = 0
        fuel = user_input * 3.785
        return

print(fuel)
'''

def conversion(gallon):
    gallon_to_litre = 3.785 * gallon
    return gallon_to_litre
if __name__ == "__main__":
    while True:
        try:
            input_gallon = float(input("Enter a number: "))
            if input_gallon < 0:
                print("Please enter a positive number, program shutting down")
                break
            else:
                converted_to_litre = conversion(input_gallon)
                print(converted_to_litre)

        except ValueError:
            print("Please enter a number")

