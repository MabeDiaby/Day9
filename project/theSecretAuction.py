from art import logo


print(logo)
bidders ={}
more_bids = False

def find_higest_bidder(bidding_rec):
    highest_bid = 0
    winner = ""
    for bidder in bidding_rec:
        bid_amount = bidding_rec[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not more_bids:
    name = input("What is your name?")
    bid = int(input("How much would you like to bid? $"))
    bidders[name] = bid
    should_continue = input("Any More bids? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        more_bids = True
        find_higest_bidder(bidders)
    elif should_continue == "yes":
        clear = print("\n"*10)


