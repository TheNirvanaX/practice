# conway's game of life
import time, copy, random, sys  # import required modules

width = 50  # actual column
height = 30  # actually row
nextCell = []
for _ in range(width):
    col = []
    for x in range(height):
        if random.randint(0, 1) == 0:
            col.append("#")  # alive cell
        else:
            col.append(" ")  # dead cell
    nextCell.append(col)
# print(nextCell)
while True:  # main loop
    print("\n" * 30)
    currentCell = copy.deepcopy(nextCell)
    for y in range(height):
        for x in range(width):
            print(currentCell[x][y], end="")
        print()
    print("press Cntrl+C to quit")

    for x in range(width):
        for y in range(height):
            # coordinate wraparound
            left = (x - 1) % width
            right = (x + 1) % width
            up = (y - 1) % height
            down = (y + 1) % height

            # update cell
            count = 0
            if currentCell[left][up] == "#":
                count += 1
            if currentCell[x][up] == "#":
                count += 1
            if currentCell[right][up] == "#":
                count += 1
            if currentCell[left][y] == "#":
                count += 1
            if currentCell[right][y] == "#":
                count += 1
            if currentCell[left][down] == "#":
                count += 1
            if currentCell[x][down] == "#":
                count += 1
            if currentCell[right][down] == "#":
                count += 1

            # update element accornding to conditions
            if currentCell[x][y] == "#" and count == (2 or 3):
                nextCell[x][y] = "#"
            elif currentCell[x][y] == " " and count == 3:
                nextCell[x][y] = "#"
            else:
                nextCell[x][y] = " "
    try:
        time.sleep(1.5)
    except KeyboardInterrupt:
        print("Conway's game of life")
        sys.exit()
