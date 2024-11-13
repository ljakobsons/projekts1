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


s = field(0.0, 1.0, 10) * 4.0
print(f"Laukums = {s}")
print(f"Relatīvā kļūda = {abs(s/math.pi-1) * 100}%")
