'''A buggy Tic-Tac-Toe game that provides an opportunity to debug code by both reasoning about it and stepping through it in a debugger.
The program has a number of bugs that are introduced one at a time. The goal is to find and fix the bugs.
Ensure you step through this program in an IDE debugger to understand how the program works and to find the bugs.'''
#TODO Add pytest to show debugging
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    """
    Print the current state of the game board.

    This function iterates over each row of the global board variable,
    printing cells separated by vertical bars and horizontal dividers between rows.

    Returns
    -------
    None
        This function only prints the board; it does not return a value.
    """
    for row_index, row in enumerate(board):
        print('|'.join(row))
        if row_index < len(board) -1:
            print('-' * 5)


def is_win(player, board_snapshot=board):
    """
    Check if the given player has won the game.

    Parameters
    ----------
    player : str
        The symbol representing the player ('X' or 'O').
    board_snapshot : list[list[str]], optional
        The current state of the board.
        Defaults to the global variable `board`.

    Returns
    -------
    bool
        True if the player has achieved a winning condition, False otherwise.
    """
    #rows
    for row_index in range(3):
        row_win = True
        for col_index in range(3):
            if board_snapshot[row_index][col_index] != player:
                row_win = False
                break
        if row_win:
            return True
    #columns
    for col_index in range(3):
        col_win = True
        for row_index in range(3):
            if board_snapshot[row_index][col_index] != player:
                col_win = False
                break
        if col_win:
            return True
    #diagonals
    if board_snapshot[0][0] == board_snapshot[1][1] == board_snapshot[2][2] == player or \
            board_snapshot[0][2] == board_snapshot[1][1] == board_snapshot[2][0] == player:
        return True

    return False

def tally_wins(results):
    # Leveraging the fact that in Python: True = 1 and False = 0 
    # we can use sum() to count the number of wins by counting all Trues and Falses
    return sum(results)


def main():
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()

        # Note that list comprehensions are more Pythonic, easier to read, and in recent versions of Python, faster.
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space (e.g., '0 2').")
            continue
        if (row < 0 or row > 2) or (col < 0 or col > 2):
            print("Invalid input! Row and column must be between 0 and 2.")
            continue
        if board[row][col] == ' ':
            board[row][col] = current_player
            win = is_win(current_player)
            results.append(win)
            if win:
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'  # Switch player
            moves += 1
        else:
            print("Cell already occupied! Try again.")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()
