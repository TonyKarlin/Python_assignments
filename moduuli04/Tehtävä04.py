# Tehtävä04
import random

tietokone = random.randint(1,10)
pelaaja = int(input("Lukusi(1-10 väliltä): "))
#print(tietokone)

while pelaaja != tietokone: # Pelaaja erisuuri kuin tietokone.

    if pelaaja > tietokone: # Suurempi
        print("Liian suuri arvaus.")
        pelaaja = int(input("Lukusi(1-10 väliltä): "))
    elif pelaaja < tietokone: # Pienempi
        print("Liian pieni arvaus.")
        pelaaja = int(input("Lukusi(1-10 väliltä): "))
else:
    print("Oikein arvattu!")


