from colorama import Fore

# Tehtävä02

"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja 
ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. 
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin 
numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."""


class Elevator:
    def __init__(self, ground_floor, top_floor):
        self.floor = ground_floor
        self.ground = ground_floor
        self.top = top_floor

    def up_a_floor(self):
        if self.floor < building1.top_floor:
            self.floor += 1
            print(f"{Fore.GREEN}Elevator going up to floor number {self.floor}{Fore.RESET}")
        else:
            print(f"{Fore.RED}You're already on the top floor ({self.floor}). You can't go any higher, so hop off.\n{Fore.RESET}")

    def down_a_floor(self):
        if self.floor > building1.ground_floor:
            self.floor -= 1
            print(f"{Fore.GREEN}Elevator going down to floor number {self.floor}{Fore.RESET}")
        else:
            print(f"{Fore.RED}You're already on the bottom floor ({self.floor}). You can't go any lower, so hop off.\n{Fore.RESET}")

    def move_to_floor(self, choose):
        if choose == self.floor:
            print(f"Elevator is already on that floor {self.floor}")
        elif choose > self.floor:
            self.print_info()
            difference = choose - self.floor
            for e in range(difference):
                self.up_a_floor()
        elif choose < self.floor:
            difference = self.floor - choose
            for e in range(difference):
                self.down_a_floor()

    def print_info(self):
        print(f"Ground floor: {self.ground}, Top floor: {self.top}\n"
              f"Current floor: {self.floor}{Fore.RESET}")


class Building:
    def __init__(self, ground_floor, top_floor, elevator_amount):
        self.ground_floor = ground_floor
        self.top_floor = top_floor
        self.elevator_amount = elevator_amount
        self.elevators = [Elevator(ground_floor, top_floor) for _ in range(elevator_amount + 1)]

    def ride_the_elevator(self, elevator_number, target_floor):
        if elevator_number < len(self.elevators):
            print(f"{Fore.BLUE}You're in elevator number {elevator_number}{Fore.RESET}")
            self.elevators[elevator_number].move_to_floor(target_floor)
            print(f"{Fore.BLUE}Elevator {elevator_number} going back down...{Fore.RESET}")
            self.elevators[elevator_number].move_to_floor(self.ground_floor)
        else:
            print(f"{Fore.RED}You're trying to use an elevator that doesn't exist!{Fore.RESET}")


building1 = Building(1, 6, 2)

building1.ride_the_elevator(2, 7)
