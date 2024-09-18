from math import sqrt

def calcDistBetweenPoints(point1_y, point1_x, point2_y, point2_x) -> float:

    if point1_x > point2_x:
        xdiff = point1_x - point2_x
    else:
        xdiff = point2_x - point1_x

    if point1_y > point2_y:
        ydiff = point1_y - point2_y
    else:
        ydiff = point2_y - point1_y

    pos_diff = sqrt(ydiff**2 + xdiff**2)

    return pos_diff
