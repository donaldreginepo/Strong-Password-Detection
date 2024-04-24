# Strong Password Detection Project by Donald Nepomuceno

import re

def is_strong_password(password):
    # Check if the password is at least eight characters long
    length_regex = re.compile(r'.{8,}')

    # Check if the password contains both uppercase and lowercase characters
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')

    # Check if the password has at least one digit
    digit_regex = re.compile(r'\d')

    # Test the password against all regex patterns
    is_long_enough = bool(length_regex.search(password))
    has_uppercase = bool(uppercase_regex.search(password))
    has_lowercase = bool(lowercase_regex.search(password))
    has_digit = bool(digit_regex.search(password))

    # Return True if all conditions are met, else return False
    return is_long_enough and has_uppercase and has_lowercase and has_digit

# Example usage
# Accept a password from the user
user_password = input("Enter a password: ")

# Call the function and print the result
if is_strong_password(user_password):
    print("Strong Password!")
else:
    print("Weak Password. Please make sure it is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.")
