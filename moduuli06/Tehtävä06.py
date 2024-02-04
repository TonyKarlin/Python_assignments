# Tehtävä06

"""Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota."""

import math


def pizza_unit_price(diameter, price):
    area = ((diameter / 2) ** 2) * math.pi / 10000
    unit_price = price / area

    return unit_price


def better_value_pizza():
    diameter1 = float(input("First pizza's diameter in (cm): "))
    price1 = float(input("First pizza's price in (euros): "))
    diameter2 = float(input("Second pizza's diameter in (cm): "))
    price2 = float(input("Second pizza's price in (euros): "))

    unit_prize1 = pizza_unit_price(diameter1, price1)
    unit_prize2 = pizza_unit_price(diameter2, price2)

    if unit_prize1 < unit_prize2:
        print("First pizza is better value for money.")
    elif unit_prize1 > unit_prize2:
        print("Second pizza is better value for money.")
    else:
        print("They are the same value for money.")


better_value_pizza()
