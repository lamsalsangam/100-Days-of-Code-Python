import os
from art import logo

print(logo)
auctioneer_list = []
closing = False


def update_dictionary(user_name, bid_amount):
    new_dictionary = {}
    new_dictionary["Name"] = user_name
    new_dictionary["Bid"] = bid_amount
    auctioneer_list.append(new_dictionary)


def comparision():
    result = 0
    name = ""
    for i in range(len(auctioneer_list)-1):
        result = auctioneer_list[i]["Bid"]
        result = auctioneer_list[i]["Name"]
        if auctioneer_list[i]["Bid"] < auctioneer_list[i+1]["Bid"]:
            result = auctioneer_list[i+1]["Bid"]
            name = auctioneer_list[i+1]["Name"]
    print(f"The highest bid is ${result} and the bidder is {name}")


while not closing:
    name = input(
        "What would you like to name yourself for the auction house?\n")
    bid = int(input("What is your bid amount?\n"))
    update_dictionary(user_name=name, bid_amount=bid)
    close = input(
        "Enter 'yes' if you wish to continue and 'no' if otherwise.\n")
    if close == "no":
        closing = True
    elif close == "yes":
        os.system("clear")

comparision()


# while not closing:
#     user_input(closing)
#     # os.system('clear')
