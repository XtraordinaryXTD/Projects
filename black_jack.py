"""Black Jack"""
import random




def deal_cards():
    """Deals card from a deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choices(deck)
    return card 


def calculate_score(cards):
    """Calculates score and checks for aces"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, pc_score):
    """Compares Scores and Declares a Winner"""

    if user_score == pc_score:
        return "Draw!"
    elif pc_score > user_score:
        return "You Lose"
    elif user_score > pc_score:
        return "You Win"
    elif user_score == 21:
        return "Black Jack, you win!"
    elif pc_score == 21:
        return "Black Jack, you lose!"
    elif pc_score > 21:
        return "You Win"
    else:
        return "You Lose"

def game():
    """The Game"""
    user_cards = []
    pc_cards = []

    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        pc_cards.append(deal_cards())


    while not game_over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print(f'{user_cards} total: {user_score}')
        print(f'{pc_cards[0]} ')   # shows only one card

        

        if user_score > 21:
            game_over = True
        else:
            another_card = input('Would you like another card? Y/N ')
            if another_card == "Y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    while pc_score !=0 and pc_score < 17:
        pc_cards.append(deal_cards())
        pc_score = calculate_score(pc_cards)
        print(f'{pc_cards} total: {pc_score}')
        print(compare(user_score, pc_score))

game()

        
        


