# program to create a password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'h', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")
set_letters = int(input("How many letters would you like to use?\n"))
set_symbols = int(input(f"How many symbols would you like to use?\n"))
set_number = int(input(f"How many numbers would you like to use?\n"))

# Method 1
"""password = ""

for char in range(1, set_letters + 1):
    password += random.choice(letters)
for char in range(1, set_symbols + 1):
    password += random.choice(symbols)
for char in range(1, set_number + 1):
    password += random.choice(numbers)

print("Your password is: {}" .format(password))"""

# Method 2(unbreakable)
password = []
for char in range(1, set_letters + 1):
    password.append(random.choice(letters))
for char in range(1, set_symbols + 1):
    password += random.choice(symbols)
for char in range(1, set_number + 1):
    password += random.choice(numbers)

random.shuffle(password)
new_password = ""
for char in password:
    new_password += char
print("Your password is: {}".format(new_password))