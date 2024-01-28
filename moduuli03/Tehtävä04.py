# Tehtävä04
vuosi = int(input("Vuosi: "))
if vuosi % 4 == 0 or vuosi % 400 == 0:
    print(f"{vuosi} on karkausvuosi.")
else:
    print(f"{vuosi} ei ole karkausvuosi.")