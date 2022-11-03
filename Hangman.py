
"""Hangman"""
import random
from turtle import position

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Constants
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
lives_stages = stages
lives = 6
game_over = False

# print(f'Hey the chosen word is {chosen_word}')


for blank in range(word_length):
    display += "_"

print(display)


if lives == 6:
    print(stages[-1])


while not game_over:
    guess = input('Choose a letter: ').lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter    
      
    
    if guess not in chosen_word:
        lives_left = lives_stages[lives]
        lives -= 1
        print(lives_left)

        if lives == 0:
            game_over = True
            print(lives_stages[0])
            print('Game Over!!!')
        
    # print(f'{lives} lives left')
    
    print(display)

    if "_" not in display:
        game_over = True
        print('You WON!!!')
    










