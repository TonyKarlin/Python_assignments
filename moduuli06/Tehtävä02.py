# Tehtävä02

"""Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion
avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa."""

import random


def dices(faces):
    result = random.randint(1, faces)
    while result != faces:
        print(f"You rolled a {result}.")
        result = random.randint(1, faces)
    print(f"You rolled a {result}! Congratulations!")
    return


max_roll = int(input("Max roll of the dice: "))
dices(max_roll)
