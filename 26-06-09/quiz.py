# ============================================================
#                      POP QUIZ
# ============================================================
# Instructions:
#   - For TRACE questions: write your answer in a comment
#   - For CODE questions: write your code below the question
#   - Do NOT use Google or any outside help
# ============================================================


# ────────────────────────────────────────────────────────────
# SECTION 1: Data Types & Variables  (6 points)
# ────────────────────────────────────────────────────────────

# Q1 - Write the data type of each value in the comment.      (3 pts)
a = 42            # type: 
b = "hello"       # type: 
c = 3.14          # type:   XX
d = True          # type:   XX
e = "99"          # type:  <-- careful!
f = int("99")     # type:  <-- careful!

# Q2 - Fix the bug so this line prints:  My score is 95       (1 pt)
score = 95
# print("My score is " + score)
 
 
# Q3 - Convert the string "7" to an integer,                  (2 pts)
#      multiply it by 3, and print the result.
number = "7"




# ────────────────────────────────────────────────────────────
# SECTION 2: Printing & Concatenation  (4 points)
# ────────────────────────────────────────────────────────────
 
# Q4 - TRACE: What does this print? Write your answer below.  (2 pts)
first = "Py"
second = "thon"
print(first + second)
print(first + " " + second)
# Answer:



# Q5 - Using the variables below, print this exact sentence:  (2 pts)
#      "I am 12 years old and I live in Canada."
#      You must use the variables — do not hardcode the values.
age = 12
country = "Canada"


# ────────────────────────────────────────────────────────────
# SECTION 3: Operators  (6 points)
# ────────────────────────────────────────────────────────────
 
# Q6 - TRACE: What does each line print? Write answers below. (3 pts)
print(17 // 3)    # Answer:
print(17 % 3)     # Answer:
print(2 ** 4)     # Answer:
 
 
# Q7 - TRACE: True or False for each line?                    (3 pts)
x = 10
y = 5
print(x > y)               # Answer:
print(x > y and y > 2)     # Answer:
print(x == 10 or y == 10)  # Answer:
print(not x == 10)         # Answer:



# ────────────────────────────────────────────────────────────
# SECTION 4: If / Else  (9 points)
# ────────────────────────────────────────────────────────────
 
# Q8 - Write code that checks if a number is positive,        (3 pts)
#      negative, or zero and prints the result.
number = -5
 
 
# Q9 - Write a grade checker.                                 (3 pts)
#      Given a score, print the letter grade:
#        90 and above → "A"
#        80 to 89     → "B"
#        70 to 79     → "C"
#        below 70     → "F"
score = 83
 
 
# Q10 - TRACE: What does this print?                          (3 pts)
age = 15
has_id = False
 
if age >= 18:
    print("Welcome!")
elif age >= 13 and has_id:
    print("Enter with adult")
else:
    print("Cannot enter")
# Answer:
 
 
# ────────────────────────────────────────────────────────────
# SECTION 5: Loops  (9 points)
# ────────────────────────────────────────────────────────────
 
# Q11 - TRACE: What does this print?                          (3 pts)
for i in range(1, 6, 2):
    print(i)
# Answer:
 
 
# Q12 - Using a while loop, print all even numbers            (3 pts)
#       from 2 to 20.
 
 
# Q13 - Using a for loop, print this pattern:                 (3 pts)
# 1
# 12
# 123
# 1234
# 12345
 
 
# ────────────────────────────────────────────────────────────
# SECTION 6: Lists  (11 points)
# ────────────────────────────────────────────────────────────
 
# Q14 - Given this list:                                      (3 pts)
colors = ["red", "blue", "green", "yellow", "purple"]
# a) Print the first item
# b) Print the last item using len() (not -1)
# c) Change "green" to "orange" and print the full list
 
 
# Q15 - Start with this list:                                 (2 pts)
animals = ["cat", "dog"]
# Add "rabbit" and "parrot" using .append()
# Then print the list and its length
 
 
# Q16 - TRACE: What does this print?                          (3 pts)
nums = [10, 20, 30, 40, 50]
nums[2] = 99
for n in nums:
    print(n)
# Answer:
 
 
# Q17 - Given this list, find and print the largest number.  (3 pts)
#       You are NOT allowed to use max().
numbers = [14, 3, 27, 8, 35, 19, 6]


# ============================================================
#                        END OF QUIZ
# ============================================================
# Total: 45 points
# ============================================================