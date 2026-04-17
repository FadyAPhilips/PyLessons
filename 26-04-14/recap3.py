def lines(lines):
    for i in range(1, lines + 1):
        if i % 5 == 0:
            print("Skip")
        else:
            print("x" * i)


lines(12)