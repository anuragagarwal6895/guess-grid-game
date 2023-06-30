import time
import sys
import os
from grid import create_grid, display_grid, generate_pairs, reveal_grid

# Main game loop


def start_game(row_count, column_count):
    # Calculate total pairs based on grid size
    total_pairs = row_count * column_count // 2

    # Create the game grid and generate pairs of numbers
    game_grid = create_grid(row_count, column_count)
    number_pairs = generate_pairs(row_count, column_count)

    # Initialize game variables
    grid_revealed = False
    player_score = 0
    guessed_pair_count = 0
    guess_count = 0

    while True:
        print("--------------------")
        print("|    PEEK-A-BOO    |")
        print("--------------------")

        # Display the game grid with revealed numbers if grid is revealed,
        # otherwise display the game grid with 'X' characters
        if grid_revealed:
            display_grid(game_grid, number_pairs)
        else:
            display_grid(game_grid, ['X'] * len(number_pairs))

        print()

        # Display menu options and get player's choice from input
        print("1. Let me select two elements")
        print("2. Uncover one element for me")
        print("3. I give up - reveal the grid")
        print("4. New game")
        print("5. Exit")

        print()

        player_choice = input("Select: ")

        # Handle invalid player choice
        if player_choice not in ['1', '2', '3', '4', '5']:
            print("Please select from the above selection only.")
            print()
            continue

        # Handle player's choice
        if player_choice == '1':
            # Check if grid is revealed before allowing player to guess a cell
            if grid_revealed:
                print("Cannot guess a cell when the grid is revealed!")
                print()
                continue

            valid_coordinates = False

            while not valid_coordinates:
                first_cell = input("Enter first cell coordinates (e.g., A1): ")
                second_cell = input(
                    "Enter second cell coordinates (e.g., B2): ")

                # Verify if the entered coordinates are valid
                if len(first_cell) != 2 or len(second_cell) != 2:
                    print("Please enter valid coordinates.")
                    print()
                    continue

                first_row = int(first_cell[1]) - 1
                first_column = ord(first_cell[0].upper()) - 65
                second_row = int(second_cell[1]) - 1
                second_column = ord(second_cell[0].upper()) - 65

                # Check if the entered coordinates are within the grid bounds
                if not (0 <= first_row < row_count and 0 <= first_column < column_count) or not (
                        0 <= second_row < row_count and 0 <= second_column < column_count):
                    print("IPlease enter valid coordinates.")
                    print()
                    continue

                # Check if the same cell is selected twice
                if (first_row, first_column) == (second_row, second_column):
                    print(
                        "Please enter different coordinates.")
                    print()
                    continue

                valid_coordinates = True

            # Check if both cells are not already revealed before revealing them and checking for a match
            if game_grid[first_row][first_column] == 'X' or game_grid[second_row][second_column] == 'X':
                game_grid[first_row][first_column] = str(
                    number_pairs[first_row * column_count + first_column])
                game_grid[second_row][second_column] = str(
                    number_pairs[second_row * column_count + second_column])

                print("Numbers Revealed")

                display_grid(game_grid, number_pairs)

                time.sleep(2)

                os.system('clear')

                # Check if cells match or not and update game variables accordingly
                if game_grid[first_row][first_column] != game_grid[second_row][second_column]:
                    guess_count += 1

                    game_grid[first_row][first_column] = 'X'
                    game_grid[second_row][second_column] = 'X'

                else:
                    guessed_pair_count += 1

                    guess_count += 1

                    game_grid[first_row][first_column] = str(
                        number_pairs[first_row * column_count + first_column])
                    game_grid[second_row][second_column] = str(
                        number_pairs[second_row * column_count + second_column])

                    if (guessed_pair_count == total_pairs):
                        player_score = 100 * (total_pairs/guess_count)
                        print(
                        f"Oh Happy Day! You have won!! Your score is: {round(player_score, 2)}")

            else:
                print("Cell already revealed!")

        elif player_choice == '2':
            # Check if grid is revealed before allowing player to manually reveal a cell
            if grid_revealed:
                print("Grid is already revealed.")
                print()
                continue

            valid_coordinates = False

            while not valid_coordinates:
                cell_to_reveal = input(
                    "Enter the cell coordinates to reveal (e.g., A1): ")

                # Verify if the entered coordinates are valid
                if len(cell_to_reveal) != 2:
                    print("Please enter valid response.")
                    print()
                    continue

                row_to_reveal = int(cell_to_reveal[1]) - 1
                column_to_reveal = ord(cell_to_reveal[0].upper()) - 65

                # Check if the entered coordinates are within the grid bounds
                if not (0 <= row_to_reveal < row_count and 0 <= column_to_reveal < column_count):
                    print("Please enter valid response.")
                    print()
                    continue

                valid_coordinates = True

            # Check if cell is not already revealed before revealing it temporarily for the player to see its value
            if game_grid[row_to_reveal][column_to_reveal] == 'X':
                game_grid[row_to_reveal][column_to_reveal] = str(
                    number_pairs[row_to_reveal * column_count + column_to_reveal])

                # print("Cell revealed!")

                os.system('clear')

                display_grid(game_grid, number_pairs)

                guess_count += 2

                if guess_count >= total_pairs * 2:
                    grid_revealed = True

                    os.system('clear')

                    print("You cheated - Loser! Your score is 0!")

            else:
                print("Cell already revealed!")

        elif player_choice == '3':
            # Check if grid is already revealed before revealing it or resetting it based on its current state
            if grid_revealed:
                os.system('clear')

                print("Grid is already revealed.")

                print()
                continue

            grid_revealed = True

            reveal_grid(game_grid, number_pairs)

            os.system('clear')

            display_grid(game_grid, number_pairs)

        elif player_choice == '4':
            os.system('clear')

            game_grid = create_grid(row_count, column_count)
            number_pairs = generate_pairs(row_count, column_count)
            grid_revealed = False
            player_score = 0
            guessed_pair_count = 0
            guess_count = 0

        elif player_choice == '5':
            sys.exit()


# Get the grid size from command line argument
grid_size_argument = int(sys.argv[1])

# Check if the grid size is valid
if grid_size_argument not in [2, 4, 6]:
    print(
        f"Invalid Grid Size {grid_size_argument}x{grid_size_argument}. Valid Grid Sizes: 2, 4, 6")
else:
    while True:
        start_game(grid_size_argument, grid_size_argument)
