import random

while True:
    # Set up the possible answers
    answers = ["rock", "paper", "scissors"]

    # Generate a random answer for the computer
    computer_answer = random.choice(answers)

    # Ask the user for their answer
    while True:
        user_answer = input("Enter rock, paper, or scissors: ")
        if user_answer in answers:
            break
        else:
            print("Error: Invalid response. Please enter rock, paper, or scissors.")

    # Check who won
    if user_answer == computer_answer:
        print("It's a tie!")
    elif user_answer == "rock" and computer_answer == "scissors":
        print("You win!")
    elif user_answer == "paper" and computer_answer == "rock":
        print("You win!")
    elif user_answer == "scissors" and computer_answer == "paper":
        print("You win!")
    else:
        print("The computer wins!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n) ")

    # If the user doesn't want to play again, break out of the loop
    if play_again.lower() not in ["y", "yes"]:
        break

# Print a thank you message
print("Thank you for playing!")