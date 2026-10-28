# Part A

stand_name = "RZK's FRESH Lemonade"
cup_price = 1
cups_per_pitcher = 10
is_open = True

print(f"===================")
print(f"{stand_name}")
print(f"{cup_price} per cup")
print(f"{cups_per_pitcher} cups per pitcher!")
print(f"===================")


# first one is string, second one is intiger, third one is intiger, 4th one is a boolean

cups_purchased = int(input("How many cups of lemonade would you like to buy?"))
amount_owed = cups_purchased * cup_price
print(f"You are purchasing {cups_purchased} cups, for {amount_owed} dollars")

amount_of_pitchers = cups_purchased // cups_per_pitcher
remainder_amount = cups_purchased % cups_per_pitcher

print(f"that is {amount_of_pitchers} pitchers, and {remainder_amount} extra cup(s)")

# / divides, it gives a decimal answer, while // floor divides, it rounds down

discount_amount = 0
if cups_purchased > 9:
    discount_amount = 0.20
elif cups_purchased > 4:
    discount_amount = 0.10
else:
    discount_amount = 0

# calulaticng_discount = discount_amount / 100
print(f"original price: {amount_owed}")
print(f"discount: {discount_amount}")
final_price = amount_owed - (amount_owed * calculating_discount)
print(f"You pay: ${final_price}")


flavors = ["Lemon", "Strawberry", "Mango", "Mint", "Peach"]
sold    = [14,       9,            22,      5,      17     ]

print(flavors)
print(sold)
sold[3] += 3
print(flavors)
print(sold)


for i in range(len(flavors)):
    print(f"{flavors[i]}: {sold[i]}")

best_seller_amount = 0
best_seller_flavor = "Yet to decide"
print("flavours that sold more than ten cups:")
for i in range(len(flavors)):
    if (sold[i]) > 10:
        print(f"{flavors[i]} sold {sold[i]} cups!")
    if sold[i] > best_seller_amount:
        best_seller_amount = sold[i]
        best_seller_flavor = flavors[i]
        

total_sold = 0
for i in range(len(flavors)):
    total_sold += sold[i]
print(f"total amount of cups sold: {total_sold}")

average_sold = total_sold / len(flavors)
print(f"average amount of cups sold per flavor: {average_sold}")

print(f"{best_seller_flavor}: {best_seller_amount}")

# tip = int(input("Enter a tip (0 to finish)"))
# total_tip = tip
# tips_recieved = 0
# while tip != 0:
#     tip = int(input("Enter a tip (0 to finish)"))
#     total_tip += tip
#     tips_recieved += 1

tips_recieved = 0
total_tip = 0
tip = int(input("Enter a tip (0 to finish)"))
while tip != 0:
    total_tip += tip
    tips_recieved += 1
    tip = int(input("Enter a tip (0 to finish)"))


print(f"Tips recieved: {tips_recieved}")
print(f"Tips total: {total_tip}")


def get_discounts(cups):
    discount_amount = 0
    if cups_purchased > 9:
        discount_amount = 20
    elif cups_purchased > 4:
        discount_amount = 10
    else:
        discount_amount = 0
    return (discount_amount)

def list_total(numbers):
    total_sold = 0
    for i in range(len(numbers)):
        total_sold += numbers[i]
    return(f"total: {total_sold}")


def best_index(numbers):
    highest_number = 0
    highest_index = 0
    for i in range(len(flavors)):
        if numbers[i] > highest_number:
            highest_number = numbers[i]
            highest_index = i
    return(highest_index)




print(f"discount: {get_discounts(7)}%")
print(list_total(sold))
print(best_index(sold))


# def day_rating(total_cups):
#     if total_cups > 79:
#         print("wow, amazing")
#     elif total_cups > 49:
#         print("grat")
#     else:
#         print("go find a bench loser")
#     return(f"ur rating is {}")


# print(day_rating(total_sold))