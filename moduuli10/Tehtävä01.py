from colorama import Fore

# Tehtävä01

"""Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h
esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta
kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai
alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen."""


class Elevator:
    def __init__(self, ground_floor, top_floor):
        self.floor = ground_floor
        self.ground = ground_floor
        self.top = top_floor

    def up_a_floor(self):
        if self.floor < 11:
            self.floor = self.floor + 1
            print(f"Elevator going up to floor number {self.floor}")
        else:
            print(f"{Fore.RED}You're already on the top floor, {self.floor}\n{Fore.RESET}")

    def down_a_floor(self):
        if self.floor > 1:
            self.floor = self.floor - 1
            print(f"Elevator going down to floor number {self.floor}")
        else:
            print(f"{Fore.RED}You're already on the bottom floor ({self.floor})\n{Fore.RESET}")

    def move_to_floor(self, choose):
        if choose == self.floor:
            print(f"Elevator is already on that floor {self.floor}")
        elif choose > self.floor:
            difference = choose - self.floor
            for e in range(difference):
                self.up_a_floor()
        elif choose < self.floor:
            difference = self.floor - choose
            for e in range(difference):
                self.down_a_floor()

    def print_info(self):
        print(f"{Fore.BLUE}Elevator status")
        print(f"Ground floor: {self.ground}, Top floor: {self.top}\n"
              f"Current floor: {self.floor}{Fore.RESET}")


elevator1 = Elevator(1, 10)

elevator1.print_info()
elevator1.move_to_floor(5)
elevator1.move_to_floor(1)

