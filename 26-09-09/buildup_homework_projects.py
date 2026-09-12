# ============================================================
#           BUILD-IT-UP HOMEWORK PROJECTS
# ============================================================
# Name: ______________________
# ============================================================
#
# There are THREE projects in this file.
#
# Each one is a single program that you build in stages.
# Do the parts IN ORDER — every part builds on the one before.
#
# Project 1 → The Pizza Shop      (easiest)
# Project 2 → The Pet Shelter     (medium)
# Project 3 → The Step Tracker    (hardest)
#
# ============================================================


# ############################################################
#
#                  PROJECT 1: THE PIZZA SHOP
#
# ############################################################
# You are building the ordering system for a pizza shop.
# ############################################################


# ────────────────────────────────────────────────────────────
# PART A — Opening the Shop
# Concepts: variables, data types, printing
# ────────────────────────────────────────────────────────────
#
# Create these variables:
#   - shop_name      → the name of your pizza shop (string)
#   - slice_price    → price of one slice, e.g. 3.50 (float)
#   - slices_per_pie → how many slices in a whole pizza, e.g. 8 (int)
#   - delivery       → whether you deliver (boolean)
#
# Print a menu header:
#
#   *****************************
#   Tony's Pizza
#   $3.5 per slice
#   8 slices per pizza
#   *****************************
#
# ANSWER IN A COMMENT: what data type is each variable?




# ────────────────────────────────────────────────────────────
# PART B — Taking an Order
# Concepts: input, type conversion, arithmetic
# ────────────────────────────────────────────────────────────
#
# Ask the customer how many slices they want.
# Calculate and print the cost:
#
#   6 slices will cost $21.0
#
# Then also calculate how many WHOLE pizzas that is,
# and how many slices are left over.
# Use // and % to do this.
#
#   That's 0 whole pizzas and 6 extra slices
#
# ANSWER IN A COMMENT: what is the difference between / and //  ?




# ────────────────────────────────────────────────────────────
# PART C — The Discount
# Concepts: if / elif / else
# ────────────────────────────────────────────────────────────
#
# Add a discount rule based on how many slices were ordered:
#
#   16 or more slices  → 20% off
#   8 to 15 slices     → 10% off
#   4 to 7 slices      → 5% off
#   fewer than 4       → no discount
#
# Print the original price, the discount, and the final price:
#
#   Original price: $21.0
#   Discount: 5%
#   You pay: $19.95




# ────────────────────────────────────────────────────────────
# PART D — Building the Order
# Concepts: while loop, lists, append()
# ────────────────────────────────────────────────────────────
#
# Now let the customer order more than one thing.
#
# Create two empty lists: order_items and order_prices
#
# Using a WHILE loop, keep asking:
#   "What topping do you want? (type 'done' to finish)"
#
# Every time they type a topping:
#   - add the topping name to order_items
#   - add a price of 1.50 to order_prices
#
# When they type "done", stop the loop.
#
# Then print how many toppings they added.




# ────────────────────────────────────────────────────────────
# PART E — Printing the Receipt
# Concepts: for loop, range(len()), parallel lists
# ────────────────────────────────────────────────────────────
#
# Using a loop over BOTH lists at the same time, print a receipt:
#
#   ------ RECEIPT ------
#   1. Pepperoni  $1.5
#   2. Mushroom   $1.5
#   3. Olives     $1.5
#   ---------------------
#
# Then add up all the topping prices (using a loop, not sum())
# and print the topping total.




# ────────────────────────────────────────────────────────────
# PART F — Functions
# Concepts: defining functions, parameters, return values
# ────────────────────────────────────────────────────────────
#
# Rewrite these as functions:
#
#   1. def get_discount(slices):
#         Takes the number of slices.
#         RETURNS the discount as a number (20, 10, 5, or 0)
#
#   2. def apply_discount(price, discount):
#         Takes a price and a discount percentage.
#         RETURNS the final price after the discount.
#
#   3. def list_total(prices):
#         Takes a list of prices.
#         RETURNS the total. (no sum() allowed)
#
# Replace your code from Parts C and E with these functions.




# ────────────────────────────────────────────────────────────
# PART G — The Full Bill  (CHALLENGE)
# Concepts: everything together
# ────────────────────────────────────────────────────────────
#
# Put it all together into one final bill:
#
#   ===== FINAL BILL =====
#   Slices (6)      : $21.0
#   Toppings (3)    : $4.5
#   Subtotal        : $25.5
#   Discount (5%)   : -$1.28
#   ----------------------
#   TOTAL           : $24.22
#   ======================
#
# Then ask the customer how much they are paying,
# and print their change. If they don't give enough money,
# print "Not enough! You still owe $X"




# ############################################################
#
#                 PROJECT 2: THE PET SHELTER
#
# ############################################################
# You are building a system to track animals at a shelter.
# ############################################################


# ────────────────────────────────────────────────────────────
# PART A — The Shelter
# Concepts: variables, data types, printing
# ────────────────────────────────────────────────────────────
#
# Create variables for:
#   - shelter_name     (string)
#   - capacity         (int)  — how many animals fit
#   - adoption_fee     (float)
#   - accepting_pets   (boolean)
#
# Print a header with all of this information in it.




# ────────────────────────────────────────────────────────────
# PART B — The Animals
# Concepts: lists, indexing, len()
# ────────────────────────────────────────────────────────────
#
# You are given these lists:

names = ["Luna", "Max", "Bella", "Rocky", "Daisy", "Milo", "Coco"]
ages =  [2,      7,     1,       9,       4,       6,      3    ]
kinds = ["cat",  "dog", "cat",   "dog",   "dog",   "cat",  "dog"]

# a) Print how many animals are in the shelter.
# b) Print the name of the FIRST animal.
# c) Print the name of the LAST animal, using len() (not -1).
# d) Print the age of the animal at index 3.
# e) Bella had a birthday! Change her age to 2 and print
#    the updated ages list.




# ────────────────────────────────────────────────────────────
# PART C — Meet the Animals
# Concepts: for loop, range(len()), parallel lists
# ────────────────────────────────────────────────────────────
#
# Using a loop over all THREE lists at the same time, print:
#
#   Luna is a 2 year old cat
#   Max is a 7 year old dog
#   Bella is a 2 year old cat
#   ...




# ────────────────────────────────────────────────────────────
# PART D — Counting and Filtering
# Concepts: if inside a loop, counters
# ────────────────────────────────────────────────────────────
#
# Using loops, calculate and print:
#   a) How many cats are in the shelter
#   b) How many dogs are in the shelter
#   c) The names of all animals older than 5
#   d) The names of all animals that are 3 or younger
#      (call these the "young ones")
#
# Example output:
#   Cats: 3
#   Dogs: 4
#   Older than 5: Max, Rocky, Milo
#   Young ones: Luna, Bella, Coco




# ────────────────────────────────────────────────────────────
# PART E — Oldest and Youngest
# Concepts: max/min without built-ins, tracking an INDEX
# ────────────────────────────────────────────────────────────
#
# Without using max() or min(), find and print:
#   - The NAME and AGE of the oldest animal
#   - The NAME and AGE of the youngest animal
#   - The average age of all animals
#
# Example output:
#   Oldest: Rocky (9 years old)
#   Youngest: Bella (2 years old)
#   Average age: 4.71...
#
# BIG HINT: to print the NAME, you can't just track the
#           biggest age — you need to track the INDEX
#           where that age was found.




# ────────────────────────────────────────────────────────────
# PART F — Life Stage
# Concepts: if / elif / else on a value
# ────────────────────────────────────────────────────────────
#
# Give each animal a life stage based on its age:
#
#   1 or younger  → "Baby"
#   2 to 4        → "Young"
#   5 to 7        → "Adult"
#   8 or older    → "Senior"
#
# Print a list like this:
#
#   Luna   (2) → Young
#   Max    (7) → Adult
#   Bella  (2) → Young
#   ...




# ────────────────────────────────────────────────────────────
# PART G — Functions
# Concepts: functions, parameters, return values
# ────────────────────────────────────────────────────────────
#
# Rewrite these as functions:
#
#   1. def life_stage(age):
#         RETURNS the life stage as a string.
#
#   2. def count_kind(kinds, kind_to_find):
#         RETURNS how many animals match that kind.
#         Example: count_kind(kinds, "cat") → 3
#
#   3. def oldest_index(ages):
#         RETURNS the INDEX of the oldest animal.
#
#   4. def average_age(ages):
#         RETURNS the average age. (no sum() allowed)
#
# Use them to rewrite Parts D, E, and F.




# ────────────────────────────────────────────────────────────
# PART H — Adoption Day  (CHALLENGE)
# Concepts: everything together, while loop, removing from a list
# ────────────────────────────────────────────────────────────
#
# Someone wants to adopt!
#
# Using a WHILE loop, keep asking:
#   "Which animal would you like to adopt? (type 'done' to stop)"
#
# For each name they type:
#   - If the name IS in the lists, print
#       "You adopted Luna the cat! That will be $75.0"
#     and add the adoption fee to a running total.
#   - If the name is NOT found, print "Sorry, we don't have that animal."
#
# When they type "done", print:
#   - How many animals they adopted
#   - The total cost
#
# Hint: to check if a name exists, loop through names and
#       compare each one.




# ############################################################
#
#                PROJECT 3: THE STEP TRACKER
#
# ############################################################
# You are building a fitness app that tracks daily steps.
# ############################################################


# ────────────────────────────────────────────────────────────
# PART A — Setting a Goal
# Concepts: variables, input, type conversion, printing
# ────────────────────────────────────────────────────────────
#
# Create a variable called user_name (ask the user for it).
# Create a variable called daily_goal (ask the user for it,
#   a number like 8000).
#
# Print:
#   Hi Alex! Your daily goal is 8000 steps.




# ────────────────────────────────────────────────────────────
# PART B — A Week of Steps
# Concepts: while loop, lists, append()
# ────────────────────────────────────────────────────────────
#
# Using a loop, ask the user for their step count for each of
# the 7 days of the week. Store them all in a list called steps.
#
#   Steps for Monday: 7200
#   Steps for Tuesday: 9100
#   ...
#
# Hint: you can make a list of day names to loop over:

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

# When you're done, print the full steps list.




# ────────────────────────────────────────────────────────────
# PART C — The Weekly Report
# Concepts: for loop, range(len()), parallel lists, if/else
# ────────────────────────────────────────────────────────────
#
# Print a report showing each day, the steps, and whether
# the goal was met:
#
#   Monday    : 7200  ✗ missed
#   Tuesday   : 9100  ✓ goal met!
#   Wednesday : 8000  ✓ goal met!
#   ...
#
# (You can use "MISSED" and "MET" instead of symbols if
#  the symbols cause problems.)




# ────────────────────────────────────────────────────────────
# PART D — The Numbers
# Concepts: accumulators, max/min without built-ins
# ────────────────────────────────────────────────────────────
#
# Without using sum(), max(), or min(), calculate and print:
#   - Total steps for the week
#   - Average steps per day
#   - The BEST day (name AND step count)
#   - The WORST day (name AND step count)
#   - How many days the goal was met
#
# Example output:
#   Total steps  : 58400
#   Daily average: 8342.86
#   Best day     : Saturday with 12000 steps
#   Worst day    : Monday with 4200 steps
#   Goals met    : 4 out of 7
#
# Remember: to get the DAY NAME, track the INDEX.




# ────────────────────────────────────────────────────────────
# PART E — The Streak  (HARD)
# Concepts: tracking state across a loop
# ────────────────────────────────────────────────────────────
#
# A "streak" is how many days IN A ROW the goal was met.
#
# Find and print the LONGEST streak in the week.
#
# Example: if the goal was met on Tue, Wed, Thu, then missed
#          Friday, then met on Sat and Sun — the longest
#          streak is 3.
#
# Print:
#   Longest streak: 3 days
#
# HINT: you need TWO variables:
#   - one for the streak you are currently counting
#   - one for the longest streak you have seen so far
#
#   Every time the goal is met, add 1 to the current streak.
#   Every time it is missed, reset the current streak to 0.
#   After each day, check if the current streak beat the record.




# ────────────────────────────────────────────────────────────
# PART F — Functions
# Concepts: functions, parameters, return values
# ────────────────────────────────────────────────────────────
#
# Rewrite these as functions:
#
#   1. def total_steps(steps):
#         RETURNS the total. (no sum() allowed)
#
#   2. def best_day_index(steps):
#         RETURNS the INDEX of the best day.
#
#   3. def goals_met(steps, goal):
#         RETURNS how many days the goal was met.
#
#   4. def longest_streak(steps, goal):
#         RETURNS the longest streak.
#
#   5. def rank(average, goal):
#         Compares the average to the goal and RETURNS a rating:
#           average >= goal          → "Champion"
#           average >= goal * 0.75   → "Doing great"
#           average >= goal * 0.5    → "Keep going"
#           below that               → "Let's start moving!"
#
# Use all five to rewrite Parts C, D, and E.




# ────────────────────────────────────────────────────────────
# PART G — The Full Dashboard  (CHALLENGE)
# Concepts: everything together
# ────────────────────────────────────────────────────────────
#
# Using all your functions, print a complete dashboard:
#
#   ========================================
#          WEEKLY REPORT FOR ALEX
#   ========================================
#   Monday    : 7200   MISSED
#   Tuesday   : 9100   MET
#   Wednesday : 8000   MET
#   Thursday  : 4200   MISSED
#   Friday    : 8800   MET
#   Saturday  : 12000  MET
#   Sunday     : 9100  MET
#   ----------------------------------------
#   Total steps   : 58400
#   Daily average : 8342.86
#   Best day      : Saturday (12000)
#   Worst day     : Thursday (4200)
#   Goals met     : 5 out of 7
#   Longest streak: 4 days
#   ----------------------------------------
#   Rating: Champion
#   ========================================
#
# BONUS: also print a simple bar chart using "*" characters,
#        where each * is 1000 steps:
#
#   Monday    : *******
#   Tuesday   : *********
#   Wednesday : ********
#
# Hint: steps // 1000 tells you how many stars to print.




# ============================================================
#                    END OF HOMEWORK
# ============================================================
# CONCEPT COVERAGE:
#
#   PIZZA SHOP    → variables, input, // and %, if/elif/else,
#                   while loops, lists, parallel lists,
#                   functions, running totals
#
#   PET SHELTER   → three parallel lists, counting, filtering,
#                   tracking an INDEX (not just a value),
#                   searching a list, functions with 2 parameters
#
#   STEP TRACKER  → building a list from input, comparing to a
#                   goal, index tracking, STREAK LOGIC (holding
#                   two variables at once), functions that call
#                   other functions
# ============================================================
