from art import logo
import  os

print(logo)
bidders = {}
new_bidders = 'yes'
while new_bidders == 'yes':

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    new_bidders = input("Are there any other bidders? 'Yes' or 'No'").lower()


if new_bidders == 'yes':
    os.system('clear')
if new_bidders == 'no':
    highest_bid = 0
    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bid = bidders[key]
        print(highest_bid)




