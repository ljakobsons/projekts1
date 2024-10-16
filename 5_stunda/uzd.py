a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x = float(input("x: "))
y = float(input("y: "))


def pieder(x, y, a, b, c):
    if a == 0 and b != 0:
        return x == -c / b
    elif a != 0 and b == 0:
        return y == -c / a
    elif a == 0 and b == 0:
        print("Tā nav taisne")
        return False
    else:
        # return True if y == m else False
        return y == -b / a * x - c / a


if pieder(x, y, a, b, c):
    print("pieder")
else:
    print("nepieder")
