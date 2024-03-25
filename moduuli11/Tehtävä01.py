# Tehtävä01

"""Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on
nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös
tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo
pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
"""


class Release:
    def __init__(self, name):
        self.name = name


class Book(Release):
    def __init__(self, author, page_amount, name):
        Release.__init__(self, name)    # super() metodin käyttö myös mahdollista
        self.author = author
        self.page_amount = page_amount

    def print_info(self):
        print(f"Release: {self.name}, {self.page_amount} pages\nAuthor: {self.author}\n")


class ComicBook(Release):
    def __init__(self, author, name):
        Release.__init__(self, name)
        self.author = author

    def print_info(self):
        print(f"Release: {self.name}\nAuthor: {self.author}\n")


comic_book1 = ComicBook("Aki Hyyppä", "Aku Ankka")
book1 = Book("Rosa Liksom", "200", "Hytti n:o 6")

comic_book1.print_info()
book1.print_info()
