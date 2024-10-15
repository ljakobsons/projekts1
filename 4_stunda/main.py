sides = input("> ").split(" ")
vertexes = len(sides)

sides = [int(i) for i in sides]

currentIndent = 0
for i in range(vertexes):
    currentIndent += sides[i]
    if currentIndent % 10 == 0:
        print(f"Vertex {i}({sides[i]}) landed on {currentIndent//10}")
    else:
        print(f"Vertex {i}({sides[i]}) landed between {currentIndent//10} and {currentIndent//10 + 1}")