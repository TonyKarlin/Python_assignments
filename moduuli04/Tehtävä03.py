# Tehtävä03
luku = float(input("Anna numero: "))

if luku != "":
    pienin = float(luku)
    suurin = float(luku)

    while luku != "":
        luku = input("Anna numero (tyhjä lopettaa): ")

        if luku != "":
            luku = float(luku)

            if luku < pienin:
                pienin = luku
            elif luku > suurin:
                suurin = luku

    print(f"Pienin luku: {pienin}\nSuurin luku: {suurin}")
else:
    print("Et antanut yhtään numeroa.")
