def polygonArea(vertices: list[ list[ float ] ]) -> int:
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0, numberOfVertices - 1):
        # Calculate the sum of multiplying each x coordinate with the y
        # coordinate in the row below
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]

        # Calculate the sum of multiplying each y coordinate with the x
        # coordinate in the row below

        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]

    # wrapping around back to the first line when you reach the bottom of the table
    sum1 = sum1 + vertices[numberOfVertices - 1][0] * vertices[0][1]
    sum2 = sum2 + vertices[0][0] * vertices[numberOfVertices - 1][1]

    # Subtract the second sum from the first,
    # get the absolute value (Absolute dfference |sum1-sum2|)
    # and divide the resulting value by 2 to get the actual
    # area of the polygon
    area = abs(sum1 - sum2) / 2

    return area
