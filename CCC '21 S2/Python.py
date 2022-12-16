# Takes in pre-requisite information
rLength = int(input())
cLength = int(input())
inpLength = int(input())

# Declares rows and columns of given length
row = [0 for i in range(rLength)]
column = [0 for i in range(cLength)]

# Takes in all the painted rows and columns
for i in range(inpLength):
    prompt, index = input().split()
    index = int(index) - 1

    if prompt == "R":
        row[index] += 1
    else:
        column[index] += 1

# If both numbers are even/odd the two paints cancelled out
goldCount = 0
for i in range(rLength):
    for j in range(cLength):
        if row[i] % 2 != column[j] % 2:
            goldCount += 1

print(goldCount)
