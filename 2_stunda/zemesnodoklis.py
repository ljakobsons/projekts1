from math import sqrt

point1_y = int(input("y1: "))
point1_x = int(input("x1: "))
point2_y = int(input("y2: "))
point2_x = int(input("x2: "))

if point1_x > point2_x:
    xdiff = point1_x - point2_x
else:
    xdiff = point2_x - point1_x

if point1_y > point2_y:
    ydiff = point1_y - point2_y
else:
    ydiff = point2_y - point1_y

pos_diff = sqrt(ydiff**2 + xdiff**2)

print(pos_diff)
