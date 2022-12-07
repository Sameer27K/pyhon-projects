import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_characters):
  # Generate the password
  password = ""
  # Create a string of all the characters we can use to generate the password
  password_characters = ""
  if use_uppercase:
    password_characters += string.ascii_uppercase
  if use_lowercase:
    password_characters += string.ascii_lowercase
  if use_numbers:
    password_characters += string.digits
  if use_special_characters:
    password_characters += string.punctuation
  # Generate the password one character at a time
  for i in range(length):
    password += random.choice(password_characters)
  return password

# Ask the user for the password length and the types of characters to include
length = int(input("Enter the password length: "))
use_uppercase = input("Include uppercase characters? (y/n): ").lower() == "y"
use_lowercase = input("Include lowercase characters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_special_characters = input("Include special characters? (y/n): ").lower() == "y"

# Generate the password
password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_characters)

# Print the password
print("Here is your random password:")
print(password)
