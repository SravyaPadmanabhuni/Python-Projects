import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'
letters_list = list(letters)
numbers_list = list(numbers)
symbols_list = list(symbols)
print('Welcome to Password Generator!!')
n_letters = int(input('How many letters you want in you password: '))
n_numbers = int(input('How many numbers you want in you password: '))
n_symbols = int(input('How many symbols you want in you password: '))
password_list = []
#for generating letters
for ch in range(n_letters):
    password_list += random.choice(letters_list)

#for generating numbers
for ch in range(n_numbers):
    password_list += random.choice(numbers_list)

#for generating symbols
for ch in range(n_symbols):
    password_list += random.choice(symbols_list)

#to shuffle list
random.shuffle(password_list)
print(''.join(password_list))
