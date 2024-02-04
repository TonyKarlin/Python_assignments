# Tehtävä03

"""Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa
paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen
litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää
negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa."""


def petrol():
    gallons = 0
    while gallons >= 0:
        gallons = float(input("Gallons of petrol: "))
        liters = gallons * 3.785
        if gallons >= 0:
            print(f"You have {liters:.2f} liters of petrol.")
        elif gallons < 0:
            print("Program terminated.")
            break
    return


petrol()
