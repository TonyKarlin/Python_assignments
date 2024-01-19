import math

#Tehtävä03

kanta = float(input("Suorakulmion kanta metreinä: "))
korkeus = float(input("Suorakulmion korkeus metreinä: "))
piiri = (kanta+kanta) + (korkeus+korkeus)
pinta_ala = kanta*korkeus
print(f"Suorakulmion piiri on: {piiri:.2f}m\nSuorakulmion pinta-ala on: {pinta_ala:.2f}m^2")
