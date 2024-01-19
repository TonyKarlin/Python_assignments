import random

def keksi_kolminumeroinen_koodi():
    return f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
def keksi_nelinumeroinen_koodi():
    return f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"

kolminumeroinen_koodi = keksi_kolminumeroinen_koodi()
nelinumeroinen_koodi = keksi_nelinumeroinen_koodi()

print(f"Kolminumeroisen lukon koodi: {kolminumeroinen_koodi}")
print(f"Nelinumeroisen lukon koodi: {nelinumeroinen_koodi}")


