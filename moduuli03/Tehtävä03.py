# Tehtävä03
sukupuoli = input("Sukupuoli: ")
hemoglobiini = int(input("Hemoglobiini(g/l): "))
if sukupuoli.lower() == "mies" and hemoglobiini < 134:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiini on korkea.")
elif sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiini on korkea")
else:
    print("Hemoglobiini on normaali")
