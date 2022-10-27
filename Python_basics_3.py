"""avg height"""

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])


# total_height = 0


# for height in student_heights:
#     total_height += height

# print(total_height)

# no_students = 0

# for measured in student_heights:
#     no_students += 1

# print(no_students)


# avg = total_height / no_students
# print(round(avg))

"""best score"""

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # print(max(student_scores)) lol

# best_score = 0
# for score in student_scores:
#     if score > best_score:
#         best_score = score
# print(f'The highest score in the class is: {best_score}')

# """even sum"""
# total = 0
# for even in range (1, 101):
#     if even % 2 == 0:
#         total += even
# print(total)

"""fizz-buzz"""
# for n in range(1, 101):
#     if n % 3 and n % 5 == 0:
#         print('fizzbuzz')
#     elif n % 3 == 0:
#         print('fizz')
#     elif n % 5 == 0:
#         print('buzz')
#     else:
#         print(n)

"""password fortress"""
import random
from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for char in range(1, nr_letters + 1):

easy_password = []

for char in range(1, nr_letters + 1):
    easy_password.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    easy_password.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    easy_password.append(random.choice(numbers))

print(easy_password) # easy

random.shuffle(easy_password)
print(easy_password) # hard

strung_pass = '' # to string

for char in easy_password:
    strung_pass += char
print(f'Your password is {strung_pass}')







