def addNumList(numList, num):

    index = 0 
    total = 0 
    
    while index < len(numList): #I still have numbers
        total += numList[index]
        index+=1

    print(total)
    print(num)

list1 = [35, 12, 1, 15, 7, 3, 5]
list2 = [11, 16, 4, 14, 40, 2, 9]

# print("I am here")
# addNumList(list1, 15)
# addNumList(list2, 4)
# print("I am there")

def add2Nums():

    num1 = int(input("what is your first number?: "))
    num2 = int(input("what is your second number?: "))

    total = num1 + num2

    print("your total is: " + str(total))


# add2Nums()

def addInputNums():

    total = 0
    NotDone = True

    while NotDone:
        num = input("what is number do you want to add? write 'done' when no more items: ")
        if num == "done":
            print("done")
            NotDone = False
        else:
            total += int(num)
        
    print("your total is: " + str(total))



print("Hello")
# addInputNums()


# animals = ["dog", "cat", "horse", "chickens"]

# def checkAnimals():
#     index = 0
#     while index < len(animals):
#         #stuff