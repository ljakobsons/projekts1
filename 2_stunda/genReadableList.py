def genPointList() -> list[list[float]]:
    coords = []
    f = open("2_stunda/punkti.txt", "r")
    raw_coords = f.readlines()

    for raw_point in raw_coords:
        point = raw_point.split(",")
        point[0] = float(point[0].strip())
        point[1] = float(point[1].strip())
        coords.append(point)

    return coords
