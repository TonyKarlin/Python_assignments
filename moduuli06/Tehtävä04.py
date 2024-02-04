# Tehtävä04

"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan."""


def calc_num_list(calc_type, numbers):
    if calc_type == 'add':
        return sum(numbers)


sum_of_numbers = calc_num_list('add', [2, 6, 8, 12])
print(f"Sum: {sum_of_numbers}")
