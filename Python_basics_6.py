"""Function with output"""

# def format_name(f_name, l_name):
#     name = f_name.title()
#     surname = l_name.title()

#     return f"Result: {name} {surname}"

# print(format_name(input('What is your first name? '), input('What is your last name ')))

"""Days in  Month"""


# def leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    


# # leap_year(2004)


# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     if leap_year(year) and month == 2:
#         return 29
#     return month_days[month - 1]
  


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

"""Calculator"""


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input('What is the first number?: '))


    for key in operations:
        print(key)

    calculating_over = True

    while calculating_over:
        num2 = float(input('What is the next number?: '))
        calculation_symbol = input("Pick an operation from the line above: ")
        calculation_function = operations[calculation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {calculation_symbol} {num2} = {result}")

        

        if input(f'Do you want another calculation with {result}? Y/N ') == "Y":
            num1 = result
        else:
            calculating_over = False
            calculator()




calculator()






    # calculation_symbol = input("Pick another operation from the line above: ")
    # num3 = int(input('What is the third number?: '))
    # calculation_function = operations[calculation_symbol]
    # result2 = calculation_function(result, num3)

    # print(f"{result2} {calculation_symbol} {num3} = {result2}")



# while not calculating_over:
#     num1 = int(input('What is the first number?: '))
#     num2 = int(input('What is the second number?: '))
#     calculation_symbol = input("Pick an operation from the line above: ")
#     proceed = input('Would you like another calculation? Y/N')
#     calculation_function = operations[calculation_symbol]
#     result = calculation_function(num1, num2)
#     if proceed == "N":
#         calculating_over = True