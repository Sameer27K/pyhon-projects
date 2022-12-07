# Define the players
player_1 = "X"
player_2 = "O"

# Define the main game loop
play_again = True
while play_again:
  # Define the game board
  board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
  ]
  current_player = player_1

  # Define the round loop
  game_over = False
  while not game_over:
    # Print the game board
    for row in board:
      print(" ".join(row))
    print()

    # Prompt the player to make a move
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    # Make the move
    if board[row][col] == "-":
      board[row][col] = current_player
      # Switch players
      if current_player == player_1:
        current_player = player_2
      else:
        current_player = player_1
    else:
      print("Invalid move, please try again.")

    # Check if the game is over
    # Check rows and columns
    for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] != "-":
        game_over = True
      if board[0][i] == board[1][i] == board[2][i] != "-":
        game_over = True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-":
      game_over = True
    if board[0][2] == board[1][1] == board[2][0] != "-":
      game_over = True

  # Print the final game board
  for row in board:
    print(" ".join(row))
  print()

  # Print the result
  if game_over:
    print(f"Player {current_player} wins!")
  else:
    print("It's a tie!")

  # Prompt the user if they want to play again
  answer = input("Do you want to play again? (y/n): ").lower()
  if answer != "y":
    play_again = False