# Tehtävä01

"""Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita
pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun
silmäluvun."""

import random

def dices():
    result = random.randint(1, 6)
    while result != 6:
        print(f"You rolled a {result}.")
        result = random.randint(1, 6)
    print(f"You rolled a {result}! Congratulations!")
    return


dices()
