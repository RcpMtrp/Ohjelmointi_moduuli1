import mysql.connector

connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='flight_game',
             user='root',
             password='M4r25q',
             autocommit=True,
             collation='utf8mb4_general_ci',
             )

def fetch_airport_by_icao(code):
    sql = (f"select name, municipality "
           f"from airport where ident= '{code}'")
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    #palauttaa monikon, jo tyhjä tulosjoukko -> none
    return result_row

user_input = input("Syötä ICAO koodi: ")
airport = fetch_airport_by_icao(user_input)

# jos airport muuttujassa on jotain muuta kuin none/Falso/0
if airport: #vastaa: airport != None
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}.")
else:
    print("Lentokenttää ei löydetty annetulla koodilla.")

# EXTRA: Tiedon lisäys
def add_airport(icao, name, municipality):
    sql = (f" INSERT INTO airport (id, ident, name, municipality) "
           f"VALUES (999, '{icao}', '{name}', '{municipality}');")
    cursor = connection.cursor()
    cursor.execute(sql)

icao = input("Anna uusi ICAO: ")
name = input("Anna uuden kentän nimi: ")
municipality = input("Ja paikkakunta: ")
add_airport(icao, name, municipality)
