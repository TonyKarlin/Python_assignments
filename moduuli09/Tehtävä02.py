# Tehtävä02

"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos
nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton
nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton
nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee
sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä
päivittää."""


class Car:
    def __init__(self, license_plate, top_speed, current_speed, distance):
        self.plate = license_plate
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

    def print_info(self):
        print(f"License plate: {self.plate}\nTop speed: {self.top_speed}km/h\n"
              f"Current speed: {self.current_speed}km/h\nDistance: {self.distance}km")


car1 = Car("ABC-123", 142, 0, 0)

cars = [car1]

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


