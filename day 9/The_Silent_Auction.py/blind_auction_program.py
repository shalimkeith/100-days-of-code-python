from replit import clear
from art import logo

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    #{"Keith": 100000 , "Prem": 987272}
    highest_amount = 0
    
    for bidder in bidding_record:
        bid_amount = bidding_record [bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The Winner Is The {winner}!!! with a bid of ${highest_amount}.")

while not bidding_finished:
    print(logo)
    name = input("Enter your name: ").strip()

    if not name:
        print("You didn't enter a name.")
    else:
        print(f"Hello, {name}!")

    price = int(input("Enter your bid : $").strip())

    if not price:
        print("You didn't enter a bid.")
    else:
        print(f"your bid is {price}$!")

    bids [name] = price
    should_continue = input(f"Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()




        