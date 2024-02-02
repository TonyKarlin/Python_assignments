# Tehtävä01
"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita
ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""

import random
dice_amount = int(input("Dices: "))

dices = []

for i in range(dice_amount):
    dices.append(random.randint(1, 6))
    print(dices)
print(f"Sum of dices: {sum(dices)}")





