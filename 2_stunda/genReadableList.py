def genPointList() -> list[ list[ float ] ]:
    coords = []
    # open the file and seperate it by lines
    f = open("2_stunda/punkti.txt", "r")
    raw_coords = f.readlines()

    for raw_point in raw_coords:

        # split the x and y coordinates into their own seperate
        # value using the "," as a splitting point
        point = raw_point.split(",")

        # strip the string variables of any extra space characters
        # and convert them into readable mathematical values
        point[0] = float(point[0].strip())
        point[1] = float(point[1].strip())

        coords.append(point)

    return coords
