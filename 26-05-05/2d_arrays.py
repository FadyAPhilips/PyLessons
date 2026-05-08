line = ["O", "X", "O", "O", "O", "X", "O"]

grid = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["P", "O", "B", "E"],
]

students = [
    ["Mark", 27, "M", 85, "loser"],
    ["Philo", 12, "M", 99, "loser"],
    ["Fady", 28, "M", 80, "loser"]
]

for student in students:
    print(student)
    if student[0] == "Philo":
        print(student[0])

board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,"W_K",0,0,0,0],
    [0,"B_R",0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ["W_B",0,0,0,0,0,0,"B_N"],
    [0,"W_P",0,0,0,0,0,0],
    [0,0,"B_K",0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

for i in range(8):
    print(board[i])
    for j in range(8):
        if board[i][j] == "B_R":
            print("white king is in postion: (" + str(i) + "," + str(j)+ ")")