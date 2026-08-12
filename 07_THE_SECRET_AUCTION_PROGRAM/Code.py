import os

from Art import logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}")


bids = {}
continue_bidding = True

while continue_bidding:

    # Name validation
    while True:
        name = input("What is your name?: ").strip()

        if name:
            break
        else:
            print("Name cannot be empty. Please enter your name.")

    if name in bids:
        print("This bidder has already placed a bid.")
        continue

    # Bid validation
    while True:
        try:
            price = int(input("What is your bid?: "))

            if price < 0:
                print("Bid cannot be negative. Please enter a valid bid.")
            else:
                break

        except ValueError:
            print("Invalid bid! Please enter a number.")

    bids[name] = price

    # Yes / No validation
    while True:
        should_continue = input(
            "Are there any other bidders? Type 'yes' or 'no'.\n"
        ).lower()

        if should_continue == "no":
            continue_bidding = False
            find_highest_bidder(bids)
            break

        elif should_continue == "yes":
            os.system("cls")
            print(logo)
            break

        else:
            print("Invalid input! Please type 'yes' or 'no'.")