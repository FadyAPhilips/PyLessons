# Q21 - Using a loop, print the times table for every number  (12 marks)
#       from 1 to 5. Format it exactly like this:
#
#       --- Times Table for 1 ---
#       1 x 1 = 1
#       1 x 2 = 2
#       ...
#       1 x 10 = 10
#
#       --- Times Table for 2 ---
#       2 x 1 = 2
#       ...


for i in range(1, 6):
    # print a whole times table
    print("")
    print(f"--- Times Table for {i} ---")
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}")