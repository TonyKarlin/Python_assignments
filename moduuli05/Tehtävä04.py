# Tehtävä04
"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien
kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain
samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
niiden läpikäymiseen."""

list_of_cities = []

for i in range(0, 5):
    city = input("Name of the city: ")
    list_of_cities.append(city)

list_of_cities = [cities.capitalize() for cities in list_of_cities]

print("List of your cities:")

for cities in list_of_cities:
    print(cities, sep="\n"[0:5])

