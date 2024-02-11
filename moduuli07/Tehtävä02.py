# Tehtävä02

"""Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin
nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö
nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa
järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen."""

names = set()
previously_entered_names = set()
name = 0

while name != "":
    name = input("Enter a name: ")

    if name in previously_entered_names:
        print(f"Previously entered name: {name}")

    else:
        if name != "":
            print(f"New name: {name}")
            previously_entered_names.add(name)
            names.add(name)

print("Set of names")
for n in names:
    print(n)


