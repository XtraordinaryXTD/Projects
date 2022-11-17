import random

EASY = 10
HARD = 5


def check_number(guess, answer, turns):
    """Check the player's guess against the random number in a set number of turns"""
    if guess > answer:
        print('Too High')
        return turns - 1
    elif guess < answer:
        print('Too Low')
        return turns - 1
    else:
        print(f'RIGHT!!! The answer was {answer}')


def difficulty():
    lives = input('Choose a difficulty. easy/hard ')
    if lives == 'hard':
        return HARD
    else:
        return EASY

def game():
    print('I am thinking of a number between 1 and 100, can you guess it?')
    answer = random.randint(1, 100)
    turns = difficulty()
    guess = 0

    while guess != answer:
        print(f'You have {turns} guesses left')
        guess = int(input('Guess a number: '))

        turns = check_number(guess, answer, turns)
        if turns == 0:
            print('Game Over!')
        elif guess != answer:
            print('Try Again')



game()