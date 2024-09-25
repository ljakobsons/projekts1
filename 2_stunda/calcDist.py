from math import sqrt


def calcDistBetweenPoints(
    point1_y: float, point1_x: float, point2_y: float, point2_x: float
) -> float:

    # get the x and y distance between the 2 points
    # on our plane
    xdiff = abs(point1_x - point2_x)
    ydiff = abs(point1_y - point2_y)

    # get the distance between the 2 points
    # via the pythagorean theorem
    pos_diff = sqrt(ydiff**2 + xdiff**2)

    return pos_diff
