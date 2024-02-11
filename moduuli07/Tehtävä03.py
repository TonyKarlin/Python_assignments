# Tehtävä03

"""Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä
syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman
syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy
ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (
ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät
koodeja helposti selaimen avulla.)"""

airports = {"EFHK": "Helsinki-Vantaa Airport", "LSZH": "Zurich Airport", "EDFH": "Frankfurt-Hahn Airport", "EDLW":
            "Dortmund Airport", "EDDM": "Munich International Airport", }

print("Do you want to input new airport details ,search for existing details, or stop the program?")

while True:

    search = input(f"INPUT (NEW/EXISTING/STOP): ")

    if search.upper() == "NEW":
        new_icao = input("Enter the ICAO-code of the airport: ")
        new_icao = new_icao.upper()
        new_name = input("Enter the name of the airport: ")
        new_name = new_name.title()
        airports.update({new_icao: new_name})
        print(f"New details for your airport saved in the system. ({new_icao}: {new_name})")

    elif search.upper() == "EXISTING":
        existing_details = input("Enter the ICAO-code of the airport: ")
        existing_details_upper = existing_details.upper()
        if existing_details_upper in airports:
            print(f"Name of the airport: {airports[existing_details_upper]}")
        else:
            print("No airports found with that ICAO-code.")
    else:
        print("You've stopped the program.")
        break

for i in airports:
    print(f"{i}: {airports[i]}")
