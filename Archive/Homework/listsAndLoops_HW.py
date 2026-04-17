#### THE BOOK EXAMPLE

# book = ["page1"]
# pageNumber = 0
# while pageNumber < len(book):
#     print(book[pageNumber])
#     pageNumber = pageNumber + 1


# Q1 - Use a loop to count how many birds are in the list - hint: will need while loop and if statments

animals = ["cat", "mouse", "bird", "dog", "bird", "fish", "cat", "hamster", "dog", "bird", "mouse", "rabbit", "bird"]

index = 0
count = 0

while index < len(animals):
    if animals[index] == "bird":
        count = count + 1
    index = index + 1

print("Number of birds is " + str(count))


# Q2
numbers = [52, 10, 11, 23, 14, 29, 19, 67, 4, 68, 5, 69, 6, 70, 7, 75, 54, 42, 28, 16, 3, 33, 43, 42]


# Q2a - print double of each number using a loop eg. for 10 print 20
# Q2b - Find the total of all the numbers added together

index = 0
total = 0

while index < len(numbers):
    print(numbers[index]*2)
    total = total + numbers[index]
    index = index + 1

print(total)

# QUESTIONS FOR NEXT TIME
# Q2c - Find the biggest and smallest numbers
# Q2d - Find me the mean of all the numbers
# Q2e - tell me which of the numbers are above average and which are below average. Hint: You might need to loop again. But I Will ask why we need to loop again.