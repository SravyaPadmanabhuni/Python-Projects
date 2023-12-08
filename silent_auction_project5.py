import os #to hide previous input 
def find_winner(bidder_details):
    highest = 0
    for bidder, price in bidder_details.items():
        if price > highest:
            highest = price
            winner = bidder 
    print('Here is all the bidder details: ', bidder_details)
    print(f'The winner is {winner} with a bid price of {highest}')

bid_data = {}
stop = False
while not stop:
    name = input('What is your name?: ')
    price = int(input('What is your bid?: '))
    bid_data[name] = price
    more_bidders = input("Are there more bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'no':
        stop = True
        find_winner(bid_data)
    elif more_bidders == 'yes':
        os.system('cls')