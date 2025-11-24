#2.3 Tuples – Basics

#A tuple is like a list, but immutable (cannot change after creation).

point = (3, 4)
print(point[0])       # 3
print(point[1])       # 4

# point[0] = 10   # ❌ Error: can't modify tuple


#Why tuples?

#Data should not change (e.g., coordinates, configuration)

#Can be used as keys in dictionaries (lists cannot)


#2.4 2D Lists (List of Lists)

#Used to represent matrices, grids, tables etc.

matrix = [
    [1, 2, 3],    # row 0
    [4, 5, 6],    # row 1
    [7, 8, 9]     # row 2
]

print(matrix[0][0])   # 1
print(matrix[1][2])   # 6


#Loop through 2D list:

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

#Take input for a 2x3 matrix:

rows = 2
cols = 3
mat = []

for i in range(rows):
    # user enters values like: 1 2 3
    row = list(map(int, input(f"Enter {cols} integers for row {i}: ").split()))
    mat.append(row)

print("Matrix:", mat)


