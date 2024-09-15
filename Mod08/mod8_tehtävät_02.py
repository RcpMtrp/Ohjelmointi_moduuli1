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




def ask_airport_count(continent, airport_size):
    sql = (f"SELECT COUNT(type) AS airport_count "
           f"FROM airport where iso_country = '{continent}' and airport.type = '{airport_size}'")
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    # print(result_row)
    # palauttaa monikon, jo tyhjä tulosjoukko -> none
    return result_row

continent = input("Anna maakoodi: ")
airport_size = input("Anna kentän koko: 'small_airport', 'medium_airport', 'large_airport' tai 'heliport' ")
#municipality = input("Ja paikkakunta: ")
airport_count = ask_airport_count(continent, airport_size)
print(airport_count)
