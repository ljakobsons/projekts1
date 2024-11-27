def y(x):
    return x**3 + 3 * x**2 - 1


a = -4
b = -1

while True:
    c = (a + b) / 2
    ya = y(a)
    yb = y(b)
    yc = y(c)
    if ya == 0:
        print(f"Sakne ir {a}")
        break
    elif yb == 0:
        print(f"Sakne ir {b}")
        break
    elif yc == 0:
        print(f"Sakne ir {c}")
        break

    if ya * yc < 0:
        b = c
    else:
        a = c

    if abs(a - b) < 0.0001:
        break
