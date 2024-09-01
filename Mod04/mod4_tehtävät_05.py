
'''
username = "python"
password = "salasana"
login_u = input("Anna käyttäjätunnus: ")
login_p = input("Anna salasana: ")

count = 0
while login_u != username:
    login_u = input("Anna käyttäjätunnus: ")
if login_u == username:
    login_p = input("Anna salasana: ")
    if login_p == password:
        print("Tervetuloa.")
else:
    print("Pääsy evätty")
'''
'''
iterator = 0
while iterator < 5:
    iterator += 1
    if iterator >= 5:
        print("Pääsy evätty.")
'''



count = 0
#username = input("Anna käyttäjätunnus: ")
#password = input("Anna salasana: ")
username = ""
password = ""
while username != "python" and password != "salasana" and count < 5:
    username = input("Anna käyttäjätunnus: ")
    password = input("Anna salasana: ")
    if username == "python" and password == "salasana":
        print("Access granted")
    else:
        print("Access denied")
        count += 1
print("Järjestelmä sulkeutuu")