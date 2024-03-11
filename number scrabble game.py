# Purpose: Number scrabble is a game that played with a list of numbers between 1 and 9.
         # Each player takes turns picking a number from the list.
         # Once a number has been picked, it cannot be picked again.
         # If a player has picked three numbers that add up to 15, that player wins the game.
         # However, if all the numbers are used and no player gets exactly 15, the game is a draw.



# Function to check if the Player wins
def win_checking (num):
    for i in range(len(num)):
        for ii in range(i + 1, len(num)):
            for iii in range(ii + 1, len(num)):
                if num[i] + num[ii] + num[iii] == 15:
                    return True

# The main function of the game
def number_scrabble_game():
    print("A) Play the game        B) Exit the game\n")
    choice = input("please enter your choice(A/B) : ").upper()
    if choice == "A" :
        # Set the game's numbers
        game_numbers = list(range(1, 10))
        player1_numbers = []
        player2_numbers = []
        
        while game_numbers:
            # Player 1 chooses a number
            print("\nPlayer 1, please choose a number from:", game_numbers)
            while True:
                try:
                    picked_number = int(input(" "))
                    if picked_number in game_numbers:
                        break
                    else:
                        print("Invalid choice. Please choose a valid number from:", game_numbers)
                except ValueError:
                    print("Invalid choice. Please choose a valid number from:", game_numbers)
                    
            # Remove the chosen number from game numbers and add it to the player's list
            game_numbers.remove(picked_number)
            player1_numbers.append(picked_number)

            # Check if Player 1 wins
            if win_checking(player1_numbers) == True:
                print("\n--------------\nPlayer 1 wins!\n--------------\n")
                number_scrabble_game()
                
            if not game_numbers:  # Check for draw after Player 1
                print("\n-----\nDraw!\n-----\n")
                number_scrabble_game()
            
            # Player 2 chooses a number
            print("\nPlayer 2, choose a number from :", game_numbers)
            while True:
                try:
                    picked_number = int(input(" "))
                    if picked_number in game_numbers:
                        break
                    else:
                        print("Invalid choice. Please choose a valid number from:", game_numbers)
                except ValueError:
                    print("Invalid choice. Please choose a valid number from:", game_numbers)

            # Remove the chosen number from game numbers and add it to the player's list
            game_numbers.remove(picked_number)
            player2_numbers.append(picked_number)

            # Check if Player 2 wins
            if win_checking(player2_numbers) == True:
                print("\n--------------\nPlayer 2 wins!\n--------------\n")
                number_scrabble_game()
            
        print("\n-----\nDraw!\n-----\n")
        number_scrabble_game()

    elif choice == "B" :
       print("\nGoodbye\n")  
       exit()
    else :
       print("Invalid choice. Please choose a valid choice\n")
       number_scrabble_game()

# start the game
print("\n           -= Welcome to Number scrabble game =-")
print("Number scrabble is a game that played with a list of numbers between 1 and 9.\nEach player takes turns picking a number from the list.\nOnce a number has been picked, it cannot be picked again.\nIf a player has picked three numbers that add up to 15, that player wins the game.\nHowever, if all the numbers are used and no player gets exactly 15, the game is a draw.\n")
result = number_scrabble_game()
print(result)