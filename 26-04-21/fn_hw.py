# ────────────────────────────────────────────────────────────
# HOMEWORK - Functions
# ────────────────────────────────────────────────────────────

# Q1 - Write a function called greet() that takes a name as a parameter
# and prints: "Hello, [name]! Welcome!"
# Call it 3 times with different names.
def greet(name):
    print("Hello, " + name + "! Welcome!")




# Q2 - Write a function called multiply() that takes two numbers
# and RETURNS their product.
# It should have a default value of 2 for the second number.
# Call it both ways:
#   - with one argument:  multiply(5)     → should return 10
#   - with two arguments: multiply(5, 4)  → should return 20
# Print both results.



# Q3 - Write a function called count_above() that takes a list of numbers
# and a threshold, and RETURNS how many numbers are above the threshold.
#
# numbers = [4, 17, 9, 25, 3, 11, 30, 8]
#
# Example calls:
#   count_above(numbers, 10)  → 3
#   count_above(numbers, 5)   → 5

def count_above(numbers, TH):
    count = 0
    for n in numbers:
        if n > TH:
            count +=1
    return count

numbers = [4, 17, 9, 25, 3, 11, 30, 8]
count = count_above(numbers, 9)

print(count)