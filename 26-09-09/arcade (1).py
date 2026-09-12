arcade_name = "RZK BILLIONARAMA" 
# string
token_price = 0.50
# float
is_open = True
#boolean
max_players = 600
# intiger

print("=============================")
print(f"Welcome to {arcade_name}!")
print(f"Buy tokens for the low low price of {token_price}")
print(f"In this INTERNATIONAL MULTI PLANET arcade, we can fit up to {max_players} at a time!")
print("=============================")

tokens_purchasing = int(input("How many tokens would you like to buy? Answer here --> "))
payment_amount = token_price * tokens_purchasing

print(f"You are purchasing {tokens_purchasing} tokens for ${payment_amount}, THANK YOU FOR COMING TO {arcade_name}!!!")
# can't multiply sequence by non-int of type 'float' 
# It sent this error message because, it cannot multiply strings, with numbers
current_tokens = 0
money_in_wallet = 10
if (money_in_wallet) >= (payment_amount):
    print(f"THANK YOU FOR SHOPPING AT {arcade_name}")
    money_in_wallet -= payment_amount
    current_tokens = tokens_purchasing
else:
    print("you cant afford this brokie, ur a loser pls leave, come back with money, AND a wing combo with bbq sauce")

print(f"You have ${money_in_wallet} in your wallet")


while (current_tokens) > 0:
    current_tokens -= 1
    print(f"Playing a game... {current_tokens} tokens left!")

print("ty for wasting ur monmey on us, and not winning anything, ur out of tokens loser, now go get a real job! Suggest us to ur friends! oh wait, i forgot, ur friendless")