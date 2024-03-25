import random

# Tehtävä02

"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on 
ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. 
Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden 
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman 
kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden 
polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan 
kolmen tunnin verran ja tulosta autojen matkamittarilukemat."""


def main():
    drive = Race("Evening drive", 8000, 2)

    while True:
        for hour in range(3):
            drive.hour_passes()

        for car in drive.cars:
            car.print_info()
        break


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


class ElectricCar(Car):
    def __init__(self, license_plate, top_speed, battery_capacity_in_kwh):
        Car.__init__(self, license_plate, top_speed, 120, 0)
        self.battery_capacity = battery_capacity_in_kwh


class GasolineCar(Car):
    def __init__(self, license_plate, top_speed, volume_in_l):
        Car.__init__(self, license_plate, top_speed, 135, 0)
        self.volume = volume_in_l


class Race:
    def __init__(self, name, length, amount_of_cars):
        self.car_amount = amount_of_cars
        self.name = name
        self.length = length
        self.cars = [ElectricCar("ABC-15", 180, 52.5)
                     if i % 2 == 0 else
                     GasolineCar("ACD-123", 180, 32.3)
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
