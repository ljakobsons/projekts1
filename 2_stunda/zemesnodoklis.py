from calcDist import calcDistBetweenPoints
from genReadableList import genPointList

points = genPointList()
per = 0

for i in range(len(points)):
    if 0 <= i + 1 < len(points):
        dist = calcDistBetweenPoints(
            points[i][0], points[i][1], points[i + 1][0], points[i + 1][0]
        )
        per += dist

print(per)
