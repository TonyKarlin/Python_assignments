# Tehtävä03

"""Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun."""
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def airport_code(icao_codes):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_codes}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result is not None:
        return result
    return None


icao_code1 = input(f"First ICAO-code: ").upper()
icao_code2 = input(f"Second ICAO-code: ").upper()
first_code = airport_code(icao_code1)
second_code = airport_code(icao_code2)

if first_code and second_code:
    first_airport = first_code[0], first_code[1]
    second_airport = second_code[0], second_code[1]
    print(f"{distance.distance(first_airport, second_airport).km:.2f}km")



