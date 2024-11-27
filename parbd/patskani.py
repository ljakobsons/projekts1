f = open("Teksts.txt", "r", encoding="UTF-8")

patskani = ["a", "e", "i", "o", "u"]

skaits = 0

for rinda in f:
    for burts in rinda:
        if burts.lower() in patskani:
            skaits += 1

print(f"Patskaņu skaits: {skaits}")

f.close()
