import math

# def paint_calc(height, width, cover):
#     area = math.ceil((height*width) / cover)
#     cover = 5
#     print(area)
    

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

"""Prime Numbers"""

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print('It\'s a prime number')
#     else:
#         print('It\'s not a prime number.')



# n = int(input("Check this number: "))
# prime_checker(number=n)

"""Caesar's Cipher"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(basic_text, position_shift, cipher_direction):
    
    caesar_cipher = ''
    position_shift = position_shift % 26
    if cipher_direction == 'decode':
        position_shift *= -1
    for letter in basic_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + position_shift
            caesar_cipher += alphabet[new_position]
        else:
            caesar_cipher += letter
    print(f'the direction is: {cipher_direction}, and the message is {caesar_cipher}')


# caesar(basic_text = text, position_shift = shift, cipher_direction = direction)

    end = True
    while not end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26
        caesar(basic_text = text, position_shift = shift, cipher_direction = direction)

        restart = print(input('Would you like to decode again??  Y/N '))

        if restart == "N":
            end = True
            print('Farewell')  
        
    
    



caesar(text, shift, direction)