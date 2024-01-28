# Tehtävä06
import random
pisteiden_maara = int(input("Pisteiden määrä: "))
N = n = 0

while N < pisteiden_maara:
    x = random.uniform (-1, 1)
    y = random.uniform (-1, 1)
    N += 1
    print(f"Arvottu piste: {x}, {y}")
    if x**2 + y**2 < 1:
        n += 1

pii = 4*n/N
print(pii)