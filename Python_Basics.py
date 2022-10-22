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
#
# c = a
# a = b
# b = c
#
#
# print("a: " + a)
# print("b: " + b)
#
# print('hello')
#
# city = (input('Where did you grew up?\n'))
# # print(city)
# pet = (input('What was the name of your first pet\n'))
# # print(pet)
#
# print(city + "" + pet + '\n')


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

# if year % 4 == 0:
#     print('Tis a leap')
# if year % 100 != 0:
#     print('Tis not')
# if year % 400 == 0:
#     print('Tis a leap')


# if year % 4 == 0 and year % 100 != 0:
#     print('leap')
# elif year % 400 == 0:
#     print('leap')
# else:
#     print('not')







# if expression1:
#    statement(s)
#    if expression2:
#       statement(s)
#    elif expression3:
#       statement(s)
#    elif expression4:
#       statement(s)
#    else:
#       statement(s)
# else:
#    statement(s)

