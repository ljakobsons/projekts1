sides = input("> ").split(" ")
requestedIndents = input("> ").split(" ")

requestedIndents = [int(i) for i in requestedIndents]

sides = [int(i) for i in sides]

currentIndent = 0
currentSide = 0
distanceCovered = 0
while True:
    if requestedIndents[0] == distanceCovered:
        print(f"Marking {requestedIndents[0]} is on vertex {currentSide+1}")
        requestedIndents.pop(0)
    elif distanceCovered + sides[currentSide] > requestedIndents[0]:
        if currentSide >= len(sides) - 1:
            print(
                f"Marking {requestedIndents[0]} is between vertex {currentSide+1} and {+1}"
            )
        else:
            print(
                f"Marking {requestedIndents[0]} is between vertex {currentSide+1} and {currentSide+2}"
            )
        requestedIndents.pop(0)
    else:
        currentSide += 1
        if currentSide >= len(sides):
            currentSide = 0

        distanceCovered += sides[currentSide]

    if len(requestedIndents) == 0:
        break
