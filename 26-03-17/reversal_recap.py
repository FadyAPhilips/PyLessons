def my_function(x, y):
  total = x / y
  return total

# Q1 - Reverse a List

# How to use Range: range( starting_point, ending_point, how_much_to_move_by )

numbers = [1, 2, 3, 4, 5, 6]

# A. Create a new list that contains the numbers in reverse order and print that list.
# You are NOT allowed to use:
# - numbers.reverse()
# - reversed()

# B. print both lists at the same time in order:
# Example output:
# 1
# 6
# 2
# 5
# ...

reversed_list = []

for i in range(len(numbers) -1, -1,-1):
    reversed_list.append(numbers[i])

print(reversed_list)


# Q2 Print this pattern using loops:

# *
# **
# ***
# ****
# *****


#~~~~~Recap Addition:
# Q1) Ask the user for an input to print the patern from the question before. the number determines how many lines of the patern are printed
# Q2) Every 5th line print the word Skip Instead of the line in the patern

# *
# **
# ***
# ****
# Skip
# ******