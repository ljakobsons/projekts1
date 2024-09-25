import turtle


def drawPolygon(points: list[float]) -> None:
    turtle.ht()
    turtle.color("green")
    turtle.penup()
    turtle.goto(points[0][0] * 50, points[0][1] * 50)
    turtle.pendown()
    for point in points:
        turtle.goto(point[0] * 50, point[1] * 50)
        turtle.dot(4, "red")
    turtle.goto(points[0][0] * 50, points[0][1] * 50)

    turtle.done()
