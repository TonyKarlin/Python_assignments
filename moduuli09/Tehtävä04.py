import random

# Tehtävä04

"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman 
alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 
100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. 
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään 
kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla 
kulje-metodia. Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan 
kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""


class Car:
    def __init__(self, registration_number, top_speed, current_speed, distance):
        self.registration = registration_number
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

    def move(self, hours):
        self.distance += hours * self.current_speed

    def print_info(self):
        print(f"Registration: {self.registration}\nTop speed: {self.top_speed} km/h\n"
              f"Current speed: {self.current_speed} km/h\nDistance: {self.distance} km\n")


cars = []

for i in range(10):
    cars.append(Car(f"ABC-{i + 1}", random.randint(100, 200), 0, 0))

# cars[0].print_info()


while True:
    for car in cars:
        if car.distance < 10000:
            car.accelerate(random.randint(-10, 15))
            car.move(1)
        else:
            break
    else:
        continue
    break

for car in cars:
    car.print_info()

