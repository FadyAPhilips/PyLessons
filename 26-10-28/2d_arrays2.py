grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# row = [1, 2, 3]

# for i in row:
#     print(i)

# print(grid)
# print(grid[1])
# print(grid[2][2])
# print(grid[0][1])

# for row in grid:
#     for i in row:
#         print(i)


# 2. Cinema seats: 1 = taken, 0 = free. 4 rows x 5 seats
seats = [
    [1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
]

total = 0
for list in seats:
    for i in list:
        if i == 1:
            total+=1

print(total)