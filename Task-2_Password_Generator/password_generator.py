# Random Password Generator
# Oasis Infobyte Internship - Python Programming

import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("===== Random Password Generator =====")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        letters = input("Include letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, letters, digits, symbols)

        if password:
            print("\nGenerated Password:", password)
        else:
            print("Error: Please select at least one character type.")

except ValueError:
    print("Invalid input! Please enter a valid number.")
