# ============================================================
#                 PYTHON TEST: THE LEMONADE STAND
# ============================================================
# Time: 1 hour
# Total: 100 marks
# ============================================================
#
# You are building a program to run a lemonade stand.
#
# This is ONE program, built in stages. Each part builds on the
# part before it, so do the parts IN ORDER.
#
# You may use your syntax cheat sheet.
# You may NOT use: sum(), max(), min(), or the internet.
#
# TIP: If you get stuck on a part, leave a comment explaining
#      what you were trying to do and move on. Partial answers
#      get partial marks.
#
# MARK BREAKDOWN:
#   Part A - Setting up the stand        10 marks 9
#   Part B - Taking an order             10 marks 10
#   Part C - The discount                10 marks 10
#   Part D - The sales board             25 marks 24
#   Part E - Tips                        15 marks 14
#   Part F - Functions                   20 marks 8
#   Part G - End of day report           10 marks 2
#                              TOTAL:   100 marks 77
# ============================================================


# ────────────────────────────────────────────────────────────
# PART A — Setting Up the Stand                     (10 marks)
# ────────────────────────────────────────────────────────────
#
# Create these variables:
#   - stand_name        → the name of your stand (string)
#   - cup_price         → price of one cup, e.g. 1.50 (float)
#   - cups_per_pitcher  → how many cups one pitcher makes, e.g. 8 (int)
#   - is_open           → whether the stand is open (boolean)
#
# Print a sign that looks like this (use your variables,
# do NOT type the values directly into the print statements):
#
#   =========================
#   Sunny Stand
#   $1.5 per cup
#   8 cups per pitcher
#   =========================
#
# ANSWER IN A COMMENT: what is the data type of each variable?
#
# (7 marks for the code, 3 marks for the data types)




# ────────────────────────────────────────────────────────────
# PART B — Taking an Order                          (10 marks)
# ────────────────────────────────────────────────────────────
#
# Ask the customer how many cups they want.
#
# Print the cost:
#   10 cups cost $15.0
#
# Then work out how many FULL pitchers that is, and how many
# EXTRA cups are left over:
#   That is 1 full pitchers and 2 extra cups
#
# ANSWER IN A COMMENT: what is the difference between / and // ?
#
# (8 marks for the code, 2 marks for the comment)




# ────────────────────────────────────────────────────────────
# PART C — The Discount                             (10 marks)
# ────────────────────────────────────────────────────────────
#
# Add a discount based on how many cups were ordered:
#
#   10 or more cups   → 20% off
#   5 to 9 cups       → 10% off
#   fewer than 5      → no discount
#
# Print the original price, the discount, and the final price:
#
#   Original price: $15.0
#   Discount: 20%
#   You pay: $12.0




# ────────────────────────────────────────────────────────────
# PART D — The Sales Board                          (25 marks)
# ────────────────────────────────────────────────────────────
#
# The stand sells 5 flavors. Here is today's data:

flavors = ["Lemon", "Strawberry", "Mango", "Mint", "Peach"]
sold    = [14,       9,            22,      5,      17     ]

# a) A late customer bought 3 more Mint cups.                (3 marks)
#    Change the Mint value in the sold list to 8,
#    then print the updated sold list.
#
# b) Using a loop, print each flavor and how many were sold: (5 marks)
#      Lemon: 14 cups
#      Strawberry: 9 cups
#      ...
#
# c) Using a loop, print only the flavors that sold          (5 marks)
#    MORE than 10 cups.
#
# d) Without using sum(), calculate and print:              (6 marks)
#      - the total cups sold
#      - the average cups sold per flavor
#
# e) Without using max(), find and print the BEST SELLER.   (6 marks)
#    Print its NAME and how many were sold:
#      Best seller: Mango (22 cups)
#
#    HINT FOR (e): printing the biggest NUMBER is not enough.
#    You need the flavor NAME too. Think about what connects
#    the two lists together.




# ────────────────────────────────────────────────────────────
# PART E — Tips                                     (15 marks)
# ────────────────────────────────────────────────────────────
#
# Customers leave tips. Using a WHILE loop, keep asking:
#
#   Enter a tip (0 to finish):
#
# Each time the user types a tip (a whole number):
#   - count it
#   - add it to a running total
#
# When the user types 0, the loop stops.
#
# Then print how many tips there were and their total:
#
#   Tips received: 3
#   Tip total: $8
#
# (the example above is what you would see if the user typed
#  2, then 5, then 1, then 0)
#
# Note: the 0 itself is NOT a tip. Do not count it.




# ────────────────────────────────────────────────────────────
# PART F — Functions                                (20 marks)
# ────────────────────────────────────────────────────────────
#
# Your program is getting long. Write these THREE functions:
#
#   1. def get_discount(cups):                          (6 marks)
#         Takes the number of cups.
#         RETURNS the discount as a number: 20, 10, or 0
#         (same rules as Part C)
#
#   2. def list_total(numbers):                         (6 marks)
#         Takes a list of numbers.
#         RETURNS the total of all the numbers.
#         (no sum() allowed)
#
#   3. def best_index(numbers):                         (8 marks)
#         Takes a list of numbers.
#         RETURNS the INDEX of the largest number.
#         (no max() allowed)
#
# Then test each function once by calling it and printing
# the result. For example, you could use the sold list:
#   print(list_total(sold))
#   print(best_index(sold))
#   print(get_discount(7))




# ────────────────────────────────────────────────────────────
# PART G — End of Day Report                        (10 marks)
# ────────────────────────────────────────────────────────────
#
# Write one more function:
#
#   def day_rating(total_cups):
#       Takes the total cups sold.
#       RETURNS a rating as a string:
#           80 or more   → "Amazing"
#           50 to 79     → "Great"
#           below 50     → "Slow"
#
# Now print a final report. You MUST use your functions
# list_total(), best_index() and day_rating() to make it:
#
#   ===== END OF DAY =====
#   Total cups sold   : 70
#   Best seller       : Mango (22 cups)
#   Average per flavor: 14.0
#   Rating            : Great
#   ======================
#
# (6 marks for the report, 4 marks for day_rating itself)




# ============================================================
#                       END OF TEST
# ============================================================
