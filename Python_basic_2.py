import random


"""Coin Toss"""
# rando_float = ((random.random()) * 5)
# print(rando_float)

# coin = random.randint(0, 1)

# if coin == 1 :
#     print('Heads')
# else:
#     print('Tails')

"""who pays the bill"""
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# x = (len(names))
# # print(x)
# rando_names = random.randint(0, x - 1) # random pozicija vo lista (-1 coz indexing starts at 0)
# # print((names[rando_names]))
# pay_bill = (names[rando_names])
# # print(pay_bill)
# print(f'{pay_bill} will pay the bill')

"""Hide the treasure"""

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0]) # 2
# vertical = int(position [1]) # 3

# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = 'X' # 3, 2
# # result
# print(f"{row1}\n{row2}\n{row3}")

""" Rock Paper Scissors """

# # art

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# choice_list = [rock, paper, scissors] 

# player_choice = int(input('Rock, Paper, Scissors, SHOOT! 0, 1, 2 :'))




# if player_choice > 2:
#     print('you cannot use a shotgun!!')
# else:
#     print(choice_list[player_choice])

#     print('VS')
#     pc_choice = random.randint(0, 2)
#     print(choice_list[pc_choice])

#     if player_choice == 0 and pc_choice == 2:
#         print('you win!')
#     elif pc_choice == 0 and player_choice == 2:
#         print('you lose')
#     elif player_choice > pc_choice:
#         print('you win!')
#     elif player_choice < pc_choice:
#         print('you lose')
#     elif player_choice == pc_choice:
#         print("it's a draw")







