# Artwork
from Art import logo

# Clear() function
import os

bid_dictionary = {}

# Methods
def bidding_process():
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    bid_dictionary[name] = bid
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if add_bidders == "yes":
        os.system('cls')
        bidding_process()

def find_winner(bids):
    max_value = 0
    for key in bids:
        if bids[key] > max_value:
            max_value = bids[key]
            winner = key
    final_list = [winner, max_value]
    return final_list

# Final program
print(logo)
print("Welcome to the secret auction program.")

bidding_process()
winner_list = find_winner(bid_dictionary)
print(f"{winner_list[0]} wins the bid with a bid of ${winner_list[1]}.")

