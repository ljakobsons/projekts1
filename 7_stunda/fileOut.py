import math


def field(a=0.0, b=1.0, n=1):
    if n == 0:
        return 0.0

    d = (b - a) / n
    s = 0.0
    x = a
    for i in range(int(n)):
        s += math.pow(x, 2)
        x += d
    return s * d


with open("7_stunda/output.txt", "w", encoding="UTF-8") as f:
    f.write("Rinķa laukums, atkarībā no intervālu skaita:")
    f.write("\n")
    f.write("n" + " " * 7 + "S" + " " * 7 + "RK(%)")
    for i in range(2, 300, 20):
        s = field(0.0, 1.0, i) * 4.0
        rk = str(round(abs(s - math.pi) / math.pi * 100))
        s = str(round(s, 3))
        f.write("\n" + str(i) + " " * (8 - len(str(i))) + s + " " * (8 - len(s)) + rk)

print("Rezultāti saglabāti failā output.txt")
