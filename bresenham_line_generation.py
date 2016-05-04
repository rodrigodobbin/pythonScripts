import sys

print("Welcome to the Bresenham's algorithm.")

print("\nLet's begin setting the size of the matrix.\n")

columns = int(input("How many columns does the matrix have?\n"))
lines = int(input("How many lines does the matrix have?\n"))

print("\nNow let's set the coordinates of two points, so we can draw a line.\n")

# Create a n*m matrix
matrix = [["." for x in range(columns)] for x in range(lines)]

# Função que liga/desliga o ponto na matrix
def connectPoints(x, y):
    matrix[lines - 1 - y][x] = "X"

# First point
x1 = int(input("Type the 'x' coordinate for the first point\n"))
y1 = int(input("Type the 'y' coordinate for the first point\n"))

# Second point
x2 = int(input("Type the 'x' coordinate for the second point\n"))
y2 = int(input("Type the 'y' coordinate for the second point\n"))

# Create variables
x = x1
y = y1
deltaX = abs(x2 - x1)
deltaY = abs(y2 - y1)
m = deltaY/deltaX
e = m - 0.5

for i in range(deltaX + 1):
    connectPoints(x, y)
    while e >= 0:
        y = y + 1
        e = e - 1

    x = x + 1
    e = e + m
    i = i + 1

print("\n")

for row in matrix:
    print(" ".join(row))
