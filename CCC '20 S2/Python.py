import math
import sys

// Takes in prerequesite information
rows = int(input())
columns = int(input())

rooms = [[None] * columns for j in range(rows)]

for i in range(rows):
    rooms[i] = input().split()

hops = [rooms[0][0]]
vis = [[False] * columns for j in range(rows)]

// Goes through all of the rooms using a breadth first approach

while len(hops) > 0:
    f1 = 1
    max = int(hops.pop())
    f2 = max

    # print("*** Factor " + str(max) + " ***")
    maxF = math.sqrt(f2)
    while f1 <= maxF:

        # print('/')
        # print(f1)
        # print(f2)

        if max % f1 == 0:
            f2 = int(max / f1)
        else:
            f1 += 1
            continue

        if f1 <= rows and f2 <= columns and not vis[f1 - 1][f2 - 1]:
            hops.append(rooms[f1 - 1][f2 - 1])
            vis[f1 - 1][f2 - 1] = True

        if f2 <= rows and f1 <= columns and not vis[f2 - 1][f1 - 1]:
            hops.append(rooms[f2 - 1][f1 - 1])
            vis[f2 - 1][f1 - 1] = True

        if f1 == rows and f2 == columns:
            print("yes")
            sys.exit()

        if f1 == columns and f2 == rows:
            print("yes")
            sys.exit()

        f1 += 1

print("no")
