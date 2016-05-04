import sys
import math

print("Welcome to the DDA's algorithm.")

print("\nLet's begin setting the size of the matrix.\n")

columns = int(input("How many columns does the matrix have?\n"))
lines = int(input("How many lines does the matrix have?\n"))

print("\nNow let's set the coordinates of two points, so we can draw a line.\n")

# Create a n*m matrix
matrix = [["." for x in range(columns)] for x in range(lines)]

# Function that turn on and off the point in the matrix
def connectPoints(x, y):
    # By default we round up the number
    # If you want to round down uncomment the math.floor() methods, and comment the math.ceil() methods
    # Remember that, this algorithm isn't very smart, so do not use the math.round() method
    x = math.ceil(x)
    y = math.ceil(y)
    # x = math.floor(x)
    # y = math.floor(y)

    matrix[lines - 1  - y][x] = "X"

# First point
x1 = int(input("Type the 'x' coordinate for the first point\n"))
y1 = int(input("Type the 'y' coordinate for the first point\n"))

# Second point
x2 = int(input("Type the 'x' coordinate for the second point\n"))
y2 = int(input("Type the 'y' coordinate for the second point\n"))

# Absolute value for x and y
xAbsValue = abs(x2 - x1)
yAbsValue = abs(y2 - y1)

# Criando variável size
# Create size variable
if xAbsValue >= yAbsValue:
    size = xAbsValue
else:
    size = yAbsValue

# Create delta x and delta y
# Verify with the size is less than zero
if size > 0:
    deltaX = xAbsValue/size
    deltaY = yAbsValue/size
else:
    print("\n please, write two distinct points.")
    sys.exit(0)

# Init the count and informations for while loop
i = 0
x = x1
y = y1

while i <= size:
    connectPoints(x, y)
    x = x + deltaX
    y = y + deltaY
    i += 1

print("\n")

for row in matrix:
    print(" ".join(row))
