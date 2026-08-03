# ============================================================
#                   WEEKLY HOMEWORK
# ============================================================
# Instructions:
#   - For TRACE questions: write your answer in a comment
#   - For CODE questions: write your code below the question
#   - Take your time — this is meant to take a full week!
# ============================================================
#
# MARK BREAKDOWN:
#   Section 1 - Data Types & Variables     15 marks
#   Section 2 - Printing & Concatenation   10 marks
#   Section 3 - Operators                  15 marks
#   Section 4 - If / Else                  20 marks
#   Section 5 - Loops                      60 marks
#   Section 6 - Lists                      80 marks
#   Section 7 - Functions                  50 marks  
#                               TOTAL:    250 marks
# ============================================================


# ────────────────────────────────────────────────────────────
# SECTION 1: Data Types & Variables  (15 marks)
# ────────────────────────────────────────────────────────────
 
# Q1 - Write the data type of each value in the comment.      (5 marks)
a = 100           # type: 
b = "100"         # type:
c = 100.0         # type:
d = False         # type:
e = str(100)      # type:
f = "Hello"       # type:
g = int("100")    # type:

 
# Q2 - Fix ALL the bugs in this code so it runs correctly.    (5 marks)
#      Do not change the variable values — only fix the errors.
name = "Alex"
age = 11
height = 1.45
 
# print("My name is " + name)
# print("I am " + age + " years old")
# print("I am " + height + "m tall")
# print("Is my age a whole number? " + type(age) == int)
 
 
# Q3 - Predict the output of each line. Write in comments.    (5 marks)
print(int(3.9))         # Answer:
print(float(5))         # Answer:
print(str(50 + 50))     # Answer:
print(int("20") + 5)    # Answer:
print(type(int("8")))   # Answer:



# ────────────────────────────────────────────────────────────
# SECTION 2: Printing & Concatenation  (10 marks)
# ────────────────────────────────────────────────────────────
 
# Q4 - Using ONLY the variables below (no hardcoding),        (5 marks)
#      print these 3 lines exactly:
#        "Player: Alex"
#        "Score: 150"
#        "Alex scored 150 points. Well done!"
player = "Alex"
score = 150
 
 
# Q5 - TRACE: What does this print? Write answers in comments.(5 marks)
word = "code"
print(word + word)
print(word * 3)
print(word[0])
print(word[2])
print(len(word))
# Answer:
 
 
 
# ────────────────────────────────────────────────────────────
# SECTION 3: Operators  (15 marks)
# ────────────────────────────────────────────────────────────
 
# Q6 - TRACE: What does each line print?                      (6 marks)
print(25 // 4)      # Answer:
print(25 % 4)       # Answer:
print(3 ** 3)       # Answer:
print(10 / 4)       # Answer:
print(10 // 4)      # Answer:
print(10 % 4)       # Answer:
 
 
# Q7 - TRACE: True or False?                                  (6 marks)
a = 8
b = 12
print(a < b and b < 20)         # Answer:
print(a > 10 or b > 10)         # Answer:
print(not a == 8)               # Answer:
print(a != b)                   # Answer:
print(a > 5 and b > 15)         # Answer:
print(not (a == 8 and b == 12)) # Answer:
 
 
# Q8 - Fill in the blank with the correct operator            (3 marks)
#      so that each print gives True.
x = 15
# print(x ___ 10)    # x is greater than 10
# print(x ___ 2 == 1)  # x divided by 2 has a remainder of 1
# print(x ___ 15)    # x is equal to 15


# ────────────────────────────────────────────────────────────
# SECTION 4: If / Else  (20 marks)
# ────────────────────────────────────────────────────────────
 
# Q9 - Write a program that asks the user for a number        (4 marks)
#      and prints:
#        "Fizz"  if it is divisible by 3
#        "Buzz"  if it is divisible by 5
#        "FizzBuzz" if it is divisible by both 3 and 5
#        The number itself if none of the above
#      Hint: think about what order to check the conditions!
 
 
# Q10 - TRACE: What does this print?                          (4 marks)
score = 72
bonus = True
 
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70 and bonus:
    print("B-")
elif score >= 70:
    print("C")
else:
    print("F")
# Answer:
 
 
# Q11 - Write a program that:                                 (6 marks)
#         - Asks the user for two numbers
#         - Prints which one is bigger
#         - If they are equal, print "They are equal"
#         - Then print whether their SUM is even or odd
 
 
# Q12 - TRACE: What does this print? Be careful!              (6 marks)
x = 10
y = 3
 
if x == 5:
    if y > 5:
        print("A")
    else:
        print("B")
else:
    if y > 5:
        print("C")
    else:
        print("D")
# Answer:
 
 

# ────────────────────────────────────────────────────────────
# SECTION 5: Loops  (60 marks)
# ────────────────────────────────────────────────────────────
 
# Q13 - TRACE: What does this print?                          (4 marks)
for i in range(0, 10, 3):
    print(i)
# Answer:
 
 
# Q14 - TRACE: What does this print?                          (4 marks)
i = 20
while i > 0:
    print(i)
    i -= 7
# Answer:
 
 
# Q15 - Using a for loop, print all multiples of 4            (4 marks)
#       from 4 to 40.
#       Expected output:
#       4
#       8
#       12
#       ...
#       40
 
 
# Q16 - Using a while loop, keep asking the user              (6 marks)
#       to enter a number until they enter 0.
#       After they enter 0, print how many numbers they entered
#       (not counting the 0).
#
#       Example:
#         Enter a number: 5
#         Enter a number: 12
#         Enter a number: 3
#         Enter a number: 0
#         You entered 3 numbers.
 
 
# Q17 - Print this pattern using loops:                       (6 marks)
#       *****
#       ****
#       ***
#       **
#       *
 
 
# Q18 - Print this pattern using loops:                       (8 marks)
#       1
#       2 2
#       3 3 3
#       4 4 4 4
#       5 5 5 5 5
 
 
# Q19 - Write a program that:                                 (8 marks)
#         - Asks the user for a number n
#         - Prints the sum of all numbers from 1 to n
#         - Prints the count of how many of those numbers are odd
#
#         Example (n = 6):
#           Sum: 21
#           Odd count: 3
 
 
# Q20 - TRACE: What does this print?                          (8 marks)
total = 0
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
    else:
        count += 1
print(total)
print(count)
# Answer:
 
 
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
 
 
# ────────────────────────────────────────────────────────────
# SECTION 6: Lists  (80 marks)
# ────────────────────────────────────────────────────────────
 
# Q22 - Given this list:                                      (6 marks)
fruits = ["apple", "banana", "cherry", "mango", "grape", "pear"]
# a) Print the item at index 3
# b) Print the last item
# c) Change "cherry" to "strawberry" and print the full list
 
 
# Q23 - Start with an empty list called playlist.             (4 marks)
#       Add these 4 songs using .append():
#       "Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine"
#       Then print the list and how many songs are in it.
 
 
# Q24 - TRACE: What does this print?                          (6 marks)
numbers = [5, 10, 15, 20, 25]
numbers[1] = numbers[1] * 2
numbers[3] = 0
print(numbers[0] + numbers[1])
print(numbers[0 + 1])
print(numbers)
print(len(numbers))
# Answer:
 
 
# Q25 - Given this list:                                      (8 marks)
scores = [45, 88, 72, 91, 55, 67, 83, 49, 76, 95]
# a) Print all scores that are 70 or above
# b) Print all scores that are below 60
# c) Count how many scores are above 80 and print that count
# d) Print the sum of all scores using a loop (no sum() allowed)
 
 
# Q26 - Given this list:                                      (8 marks)
temps = [18, 22, 30, 15, 27, 35, 19, 25, 31, 20]
# a) Find and print the highest temperature without using max()
# b) Find and print the lowest temperature without using min()
# c) Calculate and print the average temperature
 
 
# Q27 - Given this list:                                      (8 marks)
words = ["banana", "cat", "elephant", "dog", "strawberry", "ant", "watermelon", "bee"]
# a) Print only words that are longer than 4 characters. you will need to find out how to get the length of a string
# b) Print only words that are exactly 3 characters long
# c) Print the lengths of all the words (one per line)
 
 
# Q28 - TRACE: What does this print?                          (8 marks)
items = [3, 6, 9, 12, 15]
result = []
for i in range(len(items)):
    if items[i] % 2 == 0:
        result.append(items[i])
print(result)
print(len(result))
# Answer:
 
 
# Q29 - Given this list:                                      (10 marks)
numbers = [7, 2, 14, 9, 3, 18, 5, 11, 6, 16]
# a) Create a new list called evens that contains only even numbers
# b) Create a new list called odds that contains only odd numbers
# c) Print both lists
# d) Print which list is longer
 
 
# Q30 - Given this list:                                      (12 marks)
students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
grades =   [88,      72,    95,        61,       79     ]
#
# Using a loop over the two lists at the same time:
# a) Print each student's name and grade like:
#      Alice: 88
#      Bob: 72
#      ...
# b) Print the name of any student who is passing (grade >= 70)
# c) Print the name and grade of the student with the highest grade
#    (without using max())
# Hint: use range(len(students)) to loop with an index
 
 
# Q31 - Write a program that:                                 (10 marks)
#       Asks the user to enter 5 numbers one at a time.
#       Stores them all in a list.
#       Then prints:
#         - The full list
#         - The largest number (without max())
#         - The sum of all numbers
#         - All numbers that are greater than the average
 


# ────────────────────────────────────────────────────────────
# SECTION 7: Functions  (50 marks)
# ────────────────────────────────────────────────────────────
 
# Q32 - TRACE: What does this print?                          (6 marks)
def greet(name):
    return "Hello, " + name + "!"
 
def greet_twice(name):
    return greet(name) + " " + greet(name)
 
print(greet("Alex"))
print(greet_twice("Sam"))
# Answer:
 
 
# Q33 - Write a function called square() that takes a number  (4 marks)
#       and returns that number multiplied by itself.
#       Call it with 3 different numbers and print each result.
 
 
# Q34 - Write a function called is_even() that takes a number (6 marks)
#       and returns True if it is even, False if it is odd.
#       Then use it to print all even numbers from 1 to 20.
#       (Use is_even() inside your loop — don't just use % directly)
 
 
# Q35 - Write a function called grader() that takes a score   (6 marks)
#       and returns the letter grade.
#         90 and above → "A"
#         80 to 89     → "B"
#         70 to 79     → "C"
#         below 70     → "F"
#
#       Then use it to print the grade for each score in this list:
scores = [95, 82, 67, 73, 88, 55, 91]
 
 
# Q36 - TRACE: What does this print?                          (6 marks)
def mystery(a, b=10):
    result = a + b
    if result > 20:
        return result
    return 0
 
print(mystery(5))
print(mystery(5, 20))
print(mystery(15, 3))
# Answer:
 
 
# Q37 - Write a function called count_evens() that takes a    (8 marks)
#       list of numbers and returns how many are even.
#       Then write a function called count_odds() that does
#       the same for odd numbers.
#
#       Use both functions on this list and print the results:
numbers = [4, 7, 2, 9, 1, 6, 8, 3, 5, 10]
#
#       Expected output:
#         Even count: 5
#         Odd count: 5
 
 
# Q38 - Write a function called summarize() that takes a list (8 marks)
#       of numbers and prints a summary like this:
#
#         Count : 5
#         Sum   : 115
#         Avg   : 23.0
#         Max   : 35
#         Min   : 10
#
#       You are NOT allowed to use sum(), max(), or min().
#       Call it with this list:
data = [35, 10, 22, 28, 20]
 
 
# Q39 - Write a function called fizzbuzz() that takes a       (6 marks)
#       number n and prints FizzBuzz from 1 to n.
#         - Print "Fizz" if divisible by 3
#         - Print "Buzz" if divisible by 5
#         - Print "FizzBuzz" if divisible by both
#         - Otherwise print the number
#
#       Call it with n = 20.




# ============================================================
#                       END OF HOMEWORK
# ============================================================
# MARK BREAKDOWN:
#   Section 1 - Data Types & Variables     15 marks  (Q1–Q3)
#   Section 2 - Printing & Concatenation   10 marks  (Q4–Q5)
#   Section 3 - Operators                  15 marks  (Q6–Q8)
#   Section 4 - If / Else                  20 marks  (Q9–Q12)
#   Section 5 - Loops                      60 marks  (Q13–Q21)
#   Section 6 - Lists                      80 marks  (Q22–Q31)
#   Section 7 - Functions                  50 marks  (Q32–Q39)
#                               TOTAL:    250 marks
# ============================================================
 
