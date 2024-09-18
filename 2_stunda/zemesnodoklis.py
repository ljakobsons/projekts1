from calcDist import calcDistBetweenPoints
from genReadableList import genPointList
from visualize import draw_area
from calcArea import polygonArea

points = genPointList()

print("Size: ", polygonArea(points))
