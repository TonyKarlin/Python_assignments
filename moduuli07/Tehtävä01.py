# Tehtävä01

"""Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on
ensimmäinen talvikuukausi."""


seasons = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn",
           "autumn", "winter")

time_of_the_year = int(input("Number of the month (1-12): "))
month = seasons[time_of_the_year - 1]

if month == 1 or 2 or 12:
    print(f"It's {month}.")
elif month == 3 or 4 or 5:
    print(f"It's {month}.")
elif month == 6 or 7 or 8:
    print(f"It's {month}.")
elif month == 9 or 10 or 11:
    print(f"It's {month}.")
