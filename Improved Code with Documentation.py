# Strong Password Detection Project by Donald Nepomuceno

import re

def is_strong_password(password):
    """
    Determine if the provided password is strong based on multiple criteria.
    
    A strong password is defined as one that meets the following conditions:
    - At least eight characters long.
    - Contains both uppercase and lowercase letters.
    - Includes at least one numeric digit.
    
    Args:
    password (str): The password to check for strength.
    
    Returns:
    bool: True if the password is considered strong, False otherwise.
    """
    # Regex to check if the password is at least eight characters long
    length_regex = re.compile(r'.{8,}')
    # Regex to check for the presence of uppercase letters
    uppercase_regex = re.compile(r'[A-Z]')
    # Regex to check for the presence of lowercase letters
    lowercase_regex = re.compile(r'[a-z]')
    # Regex to check for the presence of at least one digit
    digit_regex = re.compile(r'\d')

    # Test the password against each regex pattern
    is_long_enough = bool(length_regex.search(password))
    has_uppercase = bool(uppercase_regex.search(password))
    has_lowercase = bool(lowercase_regex.search(password))
    has_digit = bool(digit_regex.search(password))

    # Return True if all conditions are met, else return False
    return is_long_enough and has_uppercase and has_lowercase and has_digit

# Main section to accept user input and provide feedback
if __name__ == "__main__":
    # Accept a password from the user
    user_password = input("Enter a password: ")
    
    # Call the function and print the result based on the function return value
    if is_strong_password(user_password):
        print("Strong Password!")
    else:
        print("Weak Password. Please make sure it is at least eight characters long, \
contains both uppercase and lowercase characters, and has at least one digit.")
