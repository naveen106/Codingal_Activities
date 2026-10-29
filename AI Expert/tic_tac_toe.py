import random
from colorama import init, Fore, Style

# Make colored text work consistently in the terminal.
init(autoreset=True)


# Print the nine board spaces in a 3-by-3 grid.
def display_board(board):
    print()

    # Give X, O, and empty spaces different colors.
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()


# Ask which symbol the player wants and return both symbols.
def player_choice():
    symbol = ''

    # Keep asking until the player enters X or O.
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()

    # The AI gets the other symbol.
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Ask the player for a valid, unoccupied board position.
def player_move(board, symbol):
    move = -1

    # Board positions are numbered 1-9; a digit means the space is empty.
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

    # Lists use indexes 0-8, so subtract 1 from the chosen position.
    board[move - 1] = symbol


# Choose an AI move: win if possible, otherwise block the player, otherwise pick randomly.
def ai_move(board, ai_symbol, player_symbol):
    # First, check whether the AI can win in one move.
    for i in range(9):
        if board[i].isdigit():
            # Test a copy so the real board is unchanged while checking.
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return

    # If the AI cannot win now, block any move that would let the player win.
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return

    # If there is no immediate win or block, choose any remaining space.
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol


# Return True if the given symbol has filled any winning row, column, or diagonal.
def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
        (0, 4, 8), (2, 4, 6) # Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False


# A board is full when none of its spaces still contain their original number.
def check_full(board):
    return all(not spot.isdigit() for spot in board)


# Run a game, then offer the player the option to start another one.
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        # A new board starts with its positions numbered 1 through 9.
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)

                # Check for a win before checking whether the board is full.
                if check_win(board, player_symbol):
                    display_board(board)
                    print("Congratulations! " + player_name + ", you have won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)

                # Check whether the AI won or filled the last space.
                if check_win(board, ai_symbol):
                    display_board(board)
                    print("AI has won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'Player'
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break


# Start a game only when this file is run directly, not when it is imported.
if __name__ == "__main__":
    tic_tac_toe()