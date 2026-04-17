# Q1 – While Loop Review

# Ask the user for a number.
# Print all numbers from 1 up to that number using a WHILE loop.
# If the number is divisible by 3, print "Fizz" instead of the number.

# Example:
# If the user enters 7
# Output:
# 1
# 2
# Fizz
# 4
# 5
# Fizz
# 7

# number = int(input("Enter a number: "))

# print("Output for while loop:")

# index = 1
# while index <= number:
#     if index % 3 == 0:
#         print("Fizz")
#     else:
#         print(index)
#     index += 1

# #Q2 Convert to for loop

# print("Output for for loop:")

# for potato in range(1, number+1 ):
#     if potato % 4 == 0:
#         print("Buzz")
#     else:
#         print(potato)

# names = ["John", "Peter", "James", "Sara", "Jonah"]

# for number in range(0,len(names)):
#     print(names[number])

# for name in names:
#     print(name)

# index = 0
# while index < len(names):
#     print(names[index])
#     index+=1

# PRACTICE EXERCISE

# Given this list of numbers:

# numbers = [4, 15, 22, 9, 30, 11, 18, 27]


# A) Print only the numbers that are EVEN.
# B) Count how many numbers are divisible by 3.
# C) Find the sum of all the numbers.
# D) Create a new list that only contains the numbers greater than 15.


number = int(input("Enter a number: "))

print("Output for while loop:")

index = 1
while index <= number:
    if index % 3 == 0:
        print("Fizz")
    else:
        print(index)
    index += 1


for i in range(1, number+1):
    if i % 3 == 0:
        print("Buzz")
    else:
        print(i)