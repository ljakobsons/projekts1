f = open("Teksts.txt", "r", encoding="UTF-8")

rindas = f.readlines()

for rinda in rindas:
    vskaits = 0
    rinda = rinda.strip().split()
    for vards in rinda:
        vskaits += 1
    print(vskaits)

f.close()
