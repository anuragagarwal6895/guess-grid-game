import random

# Function to display the game grid


def display_grid(game_grid, number_pairs, revealed=False):
    row_count = len(game_grid)
    column_count = len(game_grid[0])

    # Print column labels
    print("  ", end=" ")
    for column in range(column_count):
        print(f"[{chr(column + 65)}]", end=" ")
    print()

    # Print grid cells
    for row in range(row_count):
        print(f"[{row+1}]", end=" ")
        for column in range(column_count):
            if game_grid[row][column] == 'X' or (not revealed and game_grid[row][column] != 'X'):
                print(game_grid[row][column], end="  ")
            else:
                print(number_pairs[row * column_count + column], end="  ")
        print()

# Function to reveal the grid


def reveal_grid(game_grid, number_pairs):
    row_count = len(game_grid)
    column_count = len(game_grid[0])

    for row in range(row_count):
        for column in range(column_count):
            index = row * column_count + column
            game_grid[row][column] = str(number_pairs[index])

# Function to generate pairs of random numbers


def generate_pairs(row_count, column_count):
    total_pairs = (row_count * column_count) // 2
    number_pairs = [i % total_pairs for i in range(total_pairs)]
    number_pairs.extend(number_pairs)  # Duplicate pairs
    random.shuffle(number_pairs)
    return number_pairs

# Function to create the game grid


def create_grid(row_count, column_count):
    game_grid = [['X' for _ in range(column_count)] for _ in range(row_count)]
    return game_grid
