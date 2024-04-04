import requests

# Tehtävä02

"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy 
käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy 
rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä 
tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi."""


def get_lat_lon(city_name, country_code):
    response = requests.get(
        f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid=190b67e70087e2ef45fca9cf72835ade')
    data = response.json()
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        return None, None


city = input(f"Name of the City: ")
code = input(f"Country code: ")
latitude, longitude = get_lat_lon(city, code)

# print(f"Latitude: {latitude}, Longitude: {longitude}")


def get_weather(latitude, longitude):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid'
        f'=190b67e70087e2ef45fca9cf72835ade')
    data = response.json()
    temp_in_celsius = data['main']['temp'] - 273.15
    return temp_in_celsius


temperature = get_weather(latitude, longitude)
print(f"Temperature in {city}: {temperature:.2f} °C")
