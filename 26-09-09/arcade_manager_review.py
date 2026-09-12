# ============================================================
#              THE ARCADE MANAGER
#         A Build-It-Up Review Project
# ============================================================
#
# You are building a program to manage a video game arcade.
#
# IMPORTANT: Do the parts IN ORDER. Do not skip ahead.
#            Each part should still work after you add the next one.
# ============================================================


# ────────────────────────────────────────────────────────────
# PART A — Setting Up the Arcade
# Concepts: variables, data types, printing
# ────────────────────────────────────────────────────────────
#
# Create four variables:
#   - arcade_name    → the name of your arcade (a string, you pick it)
#   - token_price    → how much one token costs, e.g. 0.75 (a float)
#   - is_open        → whether the arcade is open (a boolean)
#   - max_players    → how many players can be inside, e.g. 50 (an integer)
#
# Then print a welcome banner that looks like this:
#
#   =============================
#   Welcome to Pixel Palace!
#   Tokens cost $0.75 each
#   We can fit 50 players
#   =============================
#
# You must use your variables — do not type the values directly
# into the print statements.
#
# QUESTION TO ANSWER IN A COMMENT:
#   What is the data type of each of your four variables?




# ────────────────────────────────────────────────────────────
# PART B — Buying Tokens
# Concepts: input, type conversion, operators
# ────────────────────────────────────────────────────────────
#
# Ask the player how many tokens they want to buy.
#
# Remember: input() always gives you a STRING.
# You will need to convert it before you can do math with it.
#
# Calculate the total cost (number of tokens × token_price)
# and print it like this:
#
#   You bought 8 tokens for $6.0
#
# QUESTION TO ANSWER IN A COMMENT:
#   What happens if you forget to convert the input to a number?
#   Try it and write down the error message you get.




# ────────────────────────────────────────────────────────────
# PART C — Can They Afford It?
# Concepts: if / elif / else, comparison operators
# ────────────────────────────────────────────────────────────
#
# Add a variable called wallet that holds how much money
# the player has, e.g. 5.00
#
# Now add a check BEFORE the purchase:
#   - If the total cost is less than or equal to the wallet,
#     print "Purchase successful!" and subtract the cost
#     from the wallet.
#   - If the total cost is more than the wallet,
#     print "Not enough money!" and do NOT subtract anything.
#
# Either way, print how much money is left in the wallet.
#
# Example output:
#   You want 8 tokens for $6.0
#   Not enough money!
#   You have $5.0 left




# ────────────────────────────────────────────────────────────
# PART D — The Token Counter
# Concepts: while loop
# ────────────────────────────────────────────────────────────
#
# The player is now playing games. Each game costs 1 token.
#
# Using a WHILE loop, count down the player's tokens from
# however many they bought, all the way to 0.
#
# Each time through the loop, print:
#   Playing a game... 7 tokens left
#   Playing a game... 6 tokens left
#   ...
#
# When they run out, print:
#   Out of tokens! Game over.




# ────────────────────────────────────────────────────────────
# PART E — The High Score Board
# Concepts: lists, append(), len()
# ────────────────────────────────────────────────────────────
#
# Every game the player finishes gives them a score.
#
# Start with an empty list called scores.
#
# Change your WHILE loop from Part D so that each time the
# player plays a game, you also ask them for their score
# and add it to the scores list using .append()
#
# After the loop ends, print:
#   - The full list of scores
#   - How many games they played (use len())
#
# Example output:
#   Your scores: [120, 340, 95, 500]
#   You played 4 games




# ────────────────────────────────────────────────────────────
# PART F — Reading the Score Board
# Concepts: looping through a list, indexing, if inside a loop
# ────────────────────────────────────────────────────────────
#
# Now let's look at the scores.
#
# Using a FOR loop, print every score with its game number:
#   Game 1: 120
#   Game 2: 340
#   Game 3: 95
#   Game 4: 500
#
# Then, using another loop, print only the scores that are
# above 200, like this:
#   High scores: 340
#   High scores: 500
#
# Hint: to get the game number, think about range(len(scores))




# ────────────────────────────────────────────────────────────
# PART G — Best and Worst
# Concepts: finding max/min without built-ins, accumulating totals
# ────────────────────────────────────────────────────────────
#
# Without using max(), min(), or sum(), calculate and print:
#   - The player's BEST score
#   - The player's WORST score
#   - The TOTAL of all their scores
#   - Their AVERAGE score
#
# Example output:
#   Best score : 500
#   Worst score: 95
#   Total      : 1055
#   Average    : 263.75
#
# Hint: to find the best score, start by assuming the first
#       score is the best, then check every other score
#       against it.




# ────────────────────────────────────────────────────────────
# PART H — Earning a Rank
# Concepts: if / elif / else with a calculated value
# ────────────────────────────────────────────────────────────
#
# Based on the player's AVERAGE score, give them a rank:
#
#   400 and above  → "LEGEND"
#   300 to 399     → "Pro"
#   200 to 299     → "Skilled"
#   100 to 199     → "Rookie"
#   below 100      → "Beginner"
#
# Print it like this:
#   Your rank: Skilled




# ────────────────────────────────────────────────────────────
# PART I — Turning It Into Functions
# Concepts: defining functions, parameters, return values
# ────────────────────────────────────────────────────────────
#
# Your program works — but it's getting long. Let's clean it up.
#
# Rewrite these three pieces as FUNCTIONS:
#
#   1. def best_score(scores):
#         Takes the list of scores.
#         RETURNS the highest score. (no max() allowed)
#
#   2. def average_score(scores):
#         Takes the list of scores.
#         RETURNS the average. (no sum() allowed)
#
#   3. def get_rank(average):
#         Takes an average score.
#         RETURNS the rank as a string ("LEGEND", "Pro", etc.)
#
# Then replace the code from Parts G and H with calls to
# your new functions.
#
# Your final output should look exactly the same as before —
# but now the code is much cleaner.
#
# QUESTION TO ANSWER IN A COMMENT:
#   What is the difference between a function that PRINTS
#   something and a function that RETURNS something?




# ────────────────────────────────────────────────────────────
# PART J — Multiple Players  (CHALLENGE)
# Concepts: everything together, parallel lists
# ────────────────────────────────────────────────────────────
#
# The arcade has more than one player!
#
# You are given these two lists:

players = ["Alex",  "Sam",  "Jordan", "Riley", "Casey"]
top_scores = [340,   180,    520,      95,      275   ]

# Using loops and your functions from Part I, print a
# full leaderboard:
#
#   ===== ARCADE LEADERBOARD =====
#   Alex   : 340  → Pro
#   Sam    : 180  → Rookie
#   Jordan : 520  → LEGEND
#   Riley  : 95   → Beginner
#   Casey  : 275  → Skilled
#   ==============================
#   Best player: Jordan with 520
#   Arcade average: 282.0
#
# Hint: you will need range(len(players)) to loop through
#       both lists at the same time.




# ============================================================
#                    END OF PROJECT
# ============================================================
# CONCEPTS COVERED:
#   Part A → variables, data types, printing
#   Part B → input, type conversion, arithmetic operators
#   Part C → if/elif/else, comparison operators
#   Part D → while loops
#   Part E → lists, append(), len()
#   Part F → for loops, indexing, range(len())
#   Part G → max/min without built-ins, accumulators
#   Part H → if/elif/else on a calculated value
#   Part I → functions, parameters, return values
#   Part J → parallel lists, putting it all together
# ============================================================
