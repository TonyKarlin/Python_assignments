#Tehtävä02
tuuma = 0
while tuuma >= 0:
    tuuma = float(input("Tuumat: "))
    sentit = tuuma * 2.54
    if tuuma >= 0:
        print(f"{tuuma} tuumaa on {sentit} cm.")
