# What's the Number?

if __name__ == "__main__":
    import random
    import sys

    # Generate a random number between 1 and 100
    num = random.randint(1, 100)

    # Keep track of how many guesses the user has made
    guesses = 0

    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 100: "))

    # Keep asking the user to guess the number until they guess it correctly
    while guess != num:
        # Tell the user how far off their guess was from the actual number
        if guess > num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

        # Ask the user to guess the number again
        guess = int(input("Guess a number between 1 and 100: "))

        # Increment the number of guesses the user has made
        guesses += 1

    # Tell the user how many guesses they made
    print("You guessed the number in " + str(guesses) + " guesses.")

    # Tell the user if they won a prize
    if guesses <= 10:
        print("You win a prize!")
    else:
        print("You did not win a prize.")

    # Exit the program
    sys.exit(0)