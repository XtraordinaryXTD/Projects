# """Prime Number"""

# def prime_checker(number):
#     is_prime = True
#     for i in range (2, number):
#         if number % i == 0:
#             print('not prime')
#     if is_prime:
#         print('prime')
#     else:
#         print('not')



# n = int(input("Check this number: "))
# prime_checker(number=n)

"""Ceasar's Cipher"""

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

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(basic_text = text, position_shift = shift, cipher_direction = direction)

    restart = print(input('Would you like to decode again??  Y/N '))

    if restart == "N":
        end = True
        print('Farewell')  #nadvor od looop so end isto nadvor od loop so while klauza
        
    
    



caesar(text, shift, direction)

# # def encrypt(basic_text, shift_ammount):
# #     ceasar_cipher = ''
# #     for letter in basic_text:
# #         position = alphabet.index(letter)
# #         new_position = position + shift_ammount
# #         # ciphered = alphabet[new_position]
# #         ceasar_cipher += alphabet[new_position]
# #     print(f'The encoded text is {ceasar_cipher}')
    




# # def decrypt(encrypt, shift_ammount):
# #     caesar_cipher = ''
# #     for letter in encrypt:
# #         position = alphabet.index(letter)
# #         old_position = position - shift_ammount
# #         caesar_cipher += alphabet[old_position]
# #     print(f'the decoded text is {caesar_cipher}')




