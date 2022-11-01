"""Hangman"""
import random
from turtle import position


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Hey the chosen word is {chosen_word}')

guess = input('Choose a letter: ').lower()

display = []

word_length = len(chosen_word)

for blank in range(word_length):
    display += "_"


for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter




print(display)


