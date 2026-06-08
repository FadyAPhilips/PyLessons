board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,"W_K",0,0,0,0],
    [0,"B_R",0,0,0,0,0,0,15],
    [0,0,0,0,0,0,0,0],
    ["W_B",0,0,0,0,0,0,"B_N"],
    [0,"W_P",0,0,0,0,0,0],
    [0,0,"B_K",0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]


for list in board:
    print(list[0])
    for i in range(5):
        print("Jumping Jacks")
    print(list[len(list) -1 ])
    print("~~~~~~~~~~~~~")
