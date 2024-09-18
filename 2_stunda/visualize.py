import turtle


def draw_area(points: list[float, float]) -> None:
    turtle.penup()
    turtle.goto(points[0][0] * 20, points[0][1] * 20)
    turtle.pendown()
    for point in points:
        turtle.goto(point[0] * 20, point[1] * 20)
    turtle.goto(points[0][0] * 20, points[0][1] * 20)

    turtle.done()
