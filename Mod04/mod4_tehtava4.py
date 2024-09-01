
'''username = "python"
password = "salasana"
login = input("Anna käyttäjätunnus: ")
password = "salasana"
if login == "python":
    input("Anna salasana: ")
while login != "python" and password != "salasana":
    print("Pääsy evätty.")


'''
username = "python"
password = "salasana"
login_u = input("Anna käyttäjätunnus: ")
login_p = input("Anna salasana: ")

while login_u == username:
    login_p = input("Anna salasana: ")
if login_p == password:
    print("Tervetuloa")


while player_guess != random_number:
    if player_guess > random_number:
        print("Arvauksesi on liian korkea.")
    elif player_guess < random_number:
        print("Arvauksesi on liian alhainen.")
    player_guess = float(input("Arvaa koneen arpoma luku: "))
