#Anton Nguyen encoder
def encrypt(password):
    encrypt = []                        #initializes array
    for element in password:
        element = int(element) + 3      #adds 3 to each iterated item
        encrypt.append(element)         #adds to list
    encrypt = int(''.join(str(digit) for digit in encrypt))  #converts list to integer
    return encrypt      #returns string


# Christian Garza decoder
def decoder(string):
    decoded_password = ''
    for i in string:
        digit = str(int(i) - 3)
        decoded_password += digit
    return decoded_password


while True:
    #initializes menu
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit\n''')

    #cases for 3 options
    option = int(input('Pleaser enter an option: '))
    if option == 1:
        password = (input('Please enter your password to encode: '))
        encrypted = str(encrypt(password))
        print('Your password has been encoded and stored!\n')

    if option == 2:
        print(f'The encoded password is {encrypted},', end=' ')
        print(f'and the original password is {decoder(encrypted)}.\n')

    if option == 3:
        break

