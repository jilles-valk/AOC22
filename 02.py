f = open("02_input.txt")
pointsA = 0
lines = f.readlines()
for line in lines:
    op_me = line.split(" ")
    opponent = ord(op_me[0][0]) - 65
    me = ord(op_me[1][0]) - 88

    pointsA += me + 1
    if (opponent == me):
        pointsA += 3
    if ((me - opponent) % 3 == 1):
        pointsA += 6

print(pointsA)

pointsB = 0
for line in lines:
    op_me = line.split(" ")
    opponent = ord(op_me[0][0]) - 65
    result = ord(op_me[1][0]) - 88

    if result == 0: #lose
        play = (3 + (opponent - 1)) % 3
    elif result == 1: #draw
        play = opponent
        pointsB += 3
    elif result == 2: #win
        play = (opponent + 1) % 3
        pointsB += 6

    pointsB += play + 1

print(pointsB)