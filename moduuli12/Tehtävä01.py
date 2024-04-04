import requests

# Tehtävä01

"""Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
 Käyttäjälle on näytettävä pelkkä vitsin teksti."""


def random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    joke = response.json()
    print(f"\nRandom joke: {joke['value']}")


random_joke()
