import random
from colorama import Fore

# Tehtävä04

"""Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun 
nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, 
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. 

Luokassa on seuraavat metodit:
tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo 
kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia. 
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna. 
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False. 

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan 
kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla 
toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu 
ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen 
jälkeen, kun kilpailu on päättynyt."""


def main():
    race = Race("Grand_Demolition_Derby", 8000, 10)
    hours_passed = 0

    while not race.race_over():
        race.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            print(f"{Fore.BLUE}After {hours_passed} hours:{Fore.RESET}")
            for car in race.cars:
                car.print_info()

    winner = None
    for car in race.cars:
        if car.distance >= race.length:
            winner = car
            break

    print(f"{Fore.GREEN}After {hours_passed} hours. The Grand Demolition Derby has found it's winner!{Fore.RESET}")
    for car in race.cars:
        if car == winner:
            print(f"{Fore.YELLOW}The Winner!!")
        car.print_info()
        print(Fore.RESET)


class Car:
    def __init__(self, license_plate, top_speed, current_speed, distance):
        self.plate = license_plate
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

    def move(self, hours):
        self.distance += hours * self.current_speed

    def print_info(self):
        print(f"License plate: {self.plate}\nTop speed: {self.top_speed} km/h\n"
              f"Current speed: {self.current_speed} km/h\nDistance: {self.distance} km\n")


class Race:
    def __init__(self, name, length, amount_of_cars):
        self.car_amount = amount_of_cars
        self.name = name
        self.length = length
        self.cars = [Car(f"ABC-{i + 1}", random.randint(100, 200), 0, 0)
                     for i in range(amount_of_cars)]

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.move(1)

    def race_over(self):
        for car in self.cars:
            if car.distance >= self.length:
                return True
        return False


if __name__ == "__main__":
    main()
