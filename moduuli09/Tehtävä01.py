# Tehtävä01

"""Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""


class Car:
    def __init__(self, license_plate, top_speed, current_speed, distance):
        self.plate = license_plate
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance = distance

    def print_info(self):
        print(f"License plate: {self.plate}\nTop speed: {self.top_speed}km/h\n"
              f"Current speed: {self.current_speed}km/h\nDistance: {self.distance}km")


car1 = Car("ABC-123", 142, 0, 0)

car1.print_info()
