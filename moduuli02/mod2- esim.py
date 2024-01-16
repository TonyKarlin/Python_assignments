# muuttuja ja tyyppi

age = 5
print(age)
seiska = 7
print(age + 2)

# merkkijono
age_string = "seitsemän"
# kokonaisluku
age_int = 6
# ei toimi: print(age_string + age_int)
#plus lasku
print(age_int + 4)
#merkkijonojen liittäminen (concatenation)
print(age_string + " vuotta")

#liukuluvut (float (tai double)) (ei ihan sama kuin desimaaliluku)
depth = 10.0
width = 7
area = depth * width
print(area)

# boolean: totta vai tarua (pythonissa 1 tai 0)

is_it_true = False
print(is_it_true)

# tyyppimuunnokset
age_input = input("Kuinka vanha olet?")
# print(type(age_input) # esim. "13"
age_int = int(age_input)
new_age = age_int + 1
print("Vuoden päästä olet " + str(new_age) + " vuotta vanha")
# tai "f-stringillä"
print(f"Vuoden päästä olet " +  + " vuotta vanha")

