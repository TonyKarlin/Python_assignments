# Tehtävä03

"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa
kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion
tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan
lukemaan 2090 km."""


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
        print(f"Registration: {self.registration}\nTop speed: {self.top_speed}km/h\n"
              f"Current speed: {self.current_speed}km/h\nDistance: {self.distance}km")


car1 = Car("ABC-123", 142, 0, 0)

cars = [car1]
"""
for car in cars:
    print(f"Accelerating...\n")
    car.accelerate(30)
    car.print_info()
    car.accelerate(70)
    car.print_info()
    car.accelerate(50)
    if car.current_speed > car.top_speed:
        car.current_speed = car.top_speed
    car.print_info()
    car.accelerate(-200)
    if car.current_speed < 0:
        car.current_speed = 0
    car.print_info()
"""

for car in cars:
    car.accelerate(60)
    car.print_info()
    car.move(1.5)
    car.print_info()
