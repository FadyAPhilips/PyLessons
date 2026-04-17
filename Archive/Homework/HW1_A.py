animals = ["cat", "mouse", "bird", "dog", "bird", "fish", "cat", "hamster", "dog", "bird", "mouse", "rabbit", "bird"]

index = 0
count = 0

while index < len(animals):
    if animals[index] == "bird":
        count = count + 1
    index = index + 1

print("Number of birds is " + str(count))
