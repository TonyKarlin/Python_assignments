"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
"""

numbers = 0
numbers_list = []

while numbers != "":
    numbers = input("Give a number: ")
    if numbers != "":
        numbers_list.append(int(numbers))

numbers_list.sort(reverse=True)
print(f"Descending order: {numbers_list[0:5]}")
