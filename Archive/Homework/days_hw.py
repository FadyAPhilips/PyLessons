# Q1 - A fibonacci sequence is a list of numbers, where the next number is the last two numbers added together. 
# the fibonacci sequencs always starts with 0 and 1
# example: 0, 1, 1, 2, 3, 5, 8, 13, 21. 
# create a list of numbers in the sequence up to a position that is given to the user as an input

num1 = 0
num2 = 1

#Q2 - Find out what day it is going to be in a certain number of days, given by the user from the day the user gave.
# example: if the user says today is Tuesday they want to know what day it is in 3 days, it will be Friday.

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day = input("What  day of the week is it today? ")
daysLater = int(input("how many days later do you want to find what day of the week it is? "))



#Hint: figure out what number the day that was given is first, example Wednesday is 3. then add something to it

print("It is going to be: " )