# Tehtävä02

"""Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne."""
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def airport_amount(country_code):
    sql = (f"SELECT type, COUNT(*) as amount FROM airport WHERE airport.iso_country = '{country_code}'"
           f" GROUP BY type")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_rows = cursor.fetchall()
    if cursor.rowcount > 0:
        return result_rows
    return


user_input = input("Country code: ")
user_input = user_input.upper()
amount = airport_amount(user_input)

if amount:
    print("Airport types and amounts:")
    for row in amount:
        airport_type, count = row
        print(f"{airport_type}: {count}")
else:
    print("No data found.")
