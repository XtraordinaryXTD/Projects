print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#
# answer = ['left', 'right', 'Right', 'Left']

answer = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()
if answer == 'left':
    answer1 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
          'Type "swim" to swim across. ').lower()
    if answer1 == 'wait':

        answer2 = input('You made it to the island, you enter a hovel that has 3 doors, red, blue and yellow. ').lower()

        if answer2 == 'yellow':
            print('GG')
        elif answer2 == 'red':
            print('You got burned')
        elif answer2 == 'blue':
            print('You got eaten by a rabbit')
        else:
            print('game over')
    elif answer1 == 'swim':
        print('You got attacked by the lockness monster')

else:
    print('You slid down a cliff. Game Over :(')
