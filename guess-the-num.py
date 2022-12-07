import random

# Generate a random number between 0 and 100
number = random.randint(0, 100)

# Keep track of the number of guesses the user has made
num_guesses = 0

# Keep asking the user to guess the number until they get it right
# or until they have made 5 guesses
while num_guesses < 5:
  # Get the user's guess
  guess = int(input("Enter a number between 0 and 100: "))

  # Check if the guess is too low, too high, or correct
  if guess < number:
    print("Your guess is too low.")
  elif guess > number:
    print("Your guess is too high.")
  else:
    print("You guessed the number!")
    break

  # Increment the number of guesses
  num_guesses += 1

# If the user has made 5 guesses, print the correct number and exit the program
if num_guesses == 5:
  print("You have made 5 guesses. The correct number was", number)

# Ask the user if they want to play again
play_again = input("Do you want to play again (y/n)? ")
if play_again.lower() == "y":
  # Restart the game
  print("Restarting the game...")
else:
  # Quit the game
  print("Thanks for playing!")
