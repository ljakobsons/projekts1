from calcDist import calcDistBetweenPoints
from genReadableList import genPointList
from visualize import drawPolygon
from calcArea import polygonArea

points = genPointList()

print("Size: ", str(polygonArea(points)))
# drawPolygon(points)
