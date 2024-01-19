import math

#Tehtävä05

luoti = 13.3
naula = luoti * 32
leiviskä = naula * 20

leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
massa_kg = float((leiviskät * leiviskä + naulat * naulat + luodit * luodit) / 1000)
kokonaisluku = int(massa_kg)
massa_g = massa_kg - kokonaisluku


print("Massa nykymittojen mukaan: ")
print(f"{int(massa_kg)} kilogrammaa ja {float(massa_g * 1000):.2f} grammaa.")