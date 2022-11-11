# lst = []  # prazna lista
# num = int(input('How many numbers: '))  # kolku broevi da vneses
#
# for n in range(num):
#     numbers = int(input('Enter number '))
#     lst.append(numbers)   # for loop koj gi generira broevite i gi zapisuva vo lista so .append
#
# print("Sum of elements in given list is :", sum(lst)) # print so sum funkcija na broevite zapisani vo lst
#

# num2 = input('Enter numbers: ')
#
# a = num2[0]
# b = num2[1]
#
#
# res = int(a) + int(b)
# print(res)


# print(len(input('What is your name?')))

# a = input("a: ")
# b = input("b: ")

# c = a
# a = b
# b = c


# print("a: " + a)
# print("b: " + b)

# print('hello')

city = (input('Where did you grew up?\n'))
# print(city)
pet = (input('What was the name of your first pet\n'))
# print(pet)

print(city + "" + pet + '\n')


# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = (float(weight) / float(height)**2)
# print(int(bmi))


# scr = 0
# hght = 1.92
# win = True
#
# print(f'Your score is{scr}, height is {hght} and you"re winning{win}')


# year = 365
# age = int(input('What is your current age: ')) * year
#
# week = year / 52
# month = year / 12
# death = year * 90
# when = (death - (int(age)))
# when_week = round(when / week)
# when_month = round(when / month)
#
#
# print(when_week)
# print(f'You have {when} days, {when_week} weeks,{when_month} months left')
#
#
#
# bill = float(input('What is the total bill? '))
# tip = int(input('How much tip would you like to give? 10%, 12% or 15% ')) / 100 + 1
# split = int(input('How many people would split the bill? '))
# each = round((bill / split) * tip, 2)
# print(f'Each person should pay ${each}')
#
# # tip_calculated = bill + tip

# water = int(input('Level of water'))
#
# if water > 80:
#     print('Overflow initiated')
# else:
#     print('It"s okay')
#
# number = int(input('Enter the number'))
#
# if number % 2 == 0:
#     print('the number is even ')
# else:
#     print('The number is odd ')

# check_age = int(input('What is your age? '))
#
# if check_age < 14:
#     print('Ticket price is $4')
#     gender = str(input('boy or girl'))
#     if gender == 'girl':
#         print('You ride for free')
# elif check_age <= 24:
#     print('Your Ticket price is $6')
# else:
#     print('Your Ticket price is $8')


# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = (float(weight) / float(height)**2)
# print(int(bmi)) # round it to 2 decimals?
#
# if bmi <= 18.5:
#     print('You are underweight')
# elif bmi <= 25:
#     print('You ok')
# elif bmi <= 30:
#     print('chubby')
# elif bmi <= 35:
#     print('fat')
# else:
#     print('you phat af')

# year = int(input('Which year would you like to check? '))

# if year % 4 == 0 and year % 100 != 0:
#     print('leap')
# elif year % 400 == 0:
#     print('leap')
# else:
#     print('not')

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('leap')
#         else:
#             print('not')
#     else:
#         print('leap')
# else:
#     print('not')


# height = int(input('height in cm'))
# bill = 0
#
# if height >= 120:
#     print('you can go')
#     age = int(input('your age?'))
#     if age < 12 or age > 45 and 55:
#         print('ticket 5')
#         bill = 5
#     elif age <= 18:
#         print('ticket 7')
#         bill = 7
#     else:
#         print('ticket 9')
#         bill = 9
#
#     want_photo = input('Want Photo? Y or N')
#     if want_photo == "Y":
#         bill += 3
#     print(f'Your bill is ${bill}')
# else:
#     print('cant ride shorty')


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# elif size == 'L':
#     bill += 25
#
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     elif size == 'M' or 'L':
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1
#     print(f'Your bill is ${bill}')
# else:
#     print('You have an error ordering your pizza')
#

# """Love Score Calculator powered by Shaggy™"""
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name? \n").lower()


# names = str(name1 + name2)
# T = names.count('m')
# R = names.count('a')
# U = names.count('i')
# E = names.count('b')

# true_some = str(T + R + U + E)
# # print(true_some)

# L = names.count('d')
# O = names.count('o')
# V = names.count('r')
# E = names.count('e')

# love_some = str(L + O + V + E)
# # print(love_some)

# score = int(true_some[0] + love_some[0])
# print(score)

# if score <= 10 or score >= 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif 40 <= score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f'Your score is {score}, you\'re practically soulmates')

