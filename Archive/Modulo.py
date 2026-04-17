numbers = [52, 10, 11, 23, 14, 29, 19, 67, 4, 68, 5, 69, 6, 70, 7, 75, 54, 42, 28, 16, 3, 33, 43, 42]


# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     if numbers[index] % 2 == 1:
#         index = index + 2
#     elif numbers[index] % 2 == 0:
#         index = index + 1


# 52 10 11 14 29 67 68 5 6 70 7 54 42 28 16 3 43 

## Homework
# Loop through the list of numbers and print all the numbers until you have printed 100 numbers. if you run out of
# numbers in the list. loop back again and continue printing from the start. HINT DONT use % in your while condition


index = 0
while index < 100:
    print(str(index + 1) + ": " + str(numbers[index % len(numbers)]) )
    index = index + 1

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# wednesday + 366 friday

