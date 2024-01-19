import math

#Tehtävä03

kanta = float(input("Suorakulmion kanta metreinä: "))
korkeus = float(input("Suorakulmion korkeus metreinä: "))
piiri = (kanta ** 2) + (korkeus ** 2)
pinta_ala = kanta*korkeus
print(f"Suorakulmion piiri on: {piiri:.2f}m\nSuorakulmion pinta-ala on: {pinta_ala:.2f}m^2")