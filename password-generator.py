import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '%', '$', '#', '&', '*']

letters_quantity = int(input('how many char you want?\n'))
number_quantity = int(input('how many number you want?\n'))
symbols_quantity = int(input('how many symbol you want?\n'))

password = []
for letter in range(1, letters_quantity + 1):
    password.append(random.choice(letters))

for numb in range(1, number_quantity + 1):
    password.append(random.choice(number))

for symbol in range(1, symbols_quantity + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

new_password = ""
for item in password:
    new_password += item

print(new_password)
