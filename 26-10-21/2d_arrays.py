flavors = ["Lemon", "Strawberry", "Mango", "Mint", "Peach"]
sold    = [14,       9,            22,      5,      17     ]

sales   = [flavors, sold]

def getBestSellerIndex(soldList):
    most_sold_index = 0
    for i in range(len(soldList)):
        if soldList[i] > soldList[most_sold_index]:
            most_sold_index = i
    return most_sold_index



def getBestSeller(flvList, soldList):
    most_sold_index = 0
    for i in range(len(soldList)):
        if soldList[i] > soldList[most_sold_index]:
            most_sold_index = i
    return flvList[most_sold_index]


# bestSellerIndex = getBestSellerIndex(sold)
# print(f"{getBestSeller(flavors, sold)} sold the most at {sold[bestSellerIndex]}")

print(flavors[2])
print(sales[1][2])


studentNames  = ["kevin" , "Bob" , "Mary"]
studentGrades = ["C"     , "B"   , "A" ]
studentPhones = [1234    , 2222  , 9658]

students = [studentNames, studentGrades, studentPhones]

print(students[2][1])