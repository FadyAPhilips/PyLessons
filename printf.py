# # Q17 - Given this list, find and print the largest number.  (3 pts)
# #       You are NOT allowed to use max().
# numbers = [14, 3, 27, 8, 35, 19, 6]

# biggest = 0
# for i in numbers:
#     if i > biggest:
#         biggest = i

# print(f"biggest number is: {biggest}")

Total = 3 + 1 + 3 +2 +2 +3 +3.5 + 3 + 2.5 + 3 + 3 + 2 + 0.5 +1.5 +1 +3

print(Total)

score = (Total/45)*100
print(score)

if (score) > 89:
    print("A")
elif (score) > 79:
    print("B, Youre a failure in life")
elif (score) > 69:
    print("C, You're disowned, go live on the bench outside the mall")
else:
    print("F, You were only born for the tax benefits...")