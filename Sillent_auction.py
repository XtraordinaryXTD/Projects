
# # print(logo)
bids = {}
auction_over = False

def find_highest_bidder(auction_list):
    highest_bid = 0
    winner = ' '
    for highest_bidder in auction_list:
        score = auction_list[highest_bidder]
        if score > highest_bid:
            highest_bid = score
            winner = highest_bidder
    print(f'The Winner is {highest_bidder} with a bid ammount of {highest_bid}')

while not auction_over:
    name = input('What is your name? ')
    money = int(input('How much would you like to bid? '))
    bids[name] = money
    another = input('Is there another person that would like to bid? Yes/No ')
    if another == 'No':       
        auction_over = True
        find_highest_bidder(bids)
    elif auction_over == "Yes":
        continue


