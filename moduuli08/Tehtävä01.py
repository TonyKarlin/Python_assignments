# Tehtävä01

"""Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
airport-taulun ident-sarakkeeseen."""

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def details_by_code(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    if cursor.rowcount == 1:
        return result_row
    return

user_input = 0

while user_input != "":
    user_input = input("Input your ICAO-code: ")
    user_input = user_input.upper()
    airport = details_by_code(user_input)

    if airport:
        print(f"Name of the airport: {airport[0]}\nMunicipality: {airport[1]}")
    elif user_input == "":
        print("Program terminated.")
    else:
        print("Invalid ICAO-code. Please try again.")

