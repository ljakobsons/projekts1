import math

lstdeg = [x for x in range(0, 361, 30)]

for i in lstdeg:
    print(f"{i} -> {math.sin(math.radians(i))} = {math.sin(math.radians(i)):.2f}")
