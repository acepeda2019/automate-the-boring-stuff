# TIC TAC TOE GAME
# This program generates a Tic Tac Toe board and allows a player to play against the computer.
# It evaluates at each turn whether a player has won the game or if it is a tie.
# If the user enters an invalid position, they are prompted to try again.

import pprint as pp
import random
import time

board = {
    'A1':' ', 'B1':' ', 'C3':' ',
    'A2':' ', 'B2':' ', 'B3':' ',
    'A3':' ', 'C1':' ', 'C2':' ',
}

winning_positions = [
    {'A1', 'A2', 'A3'}, {'B1', 'B2', 'B3'}, {'C1', 'C2', 'C3'}, #rows
    {'A1', 'B1', 'C1'}, {'A2', 'B2', 'C2'}, {'A3', 'B3', 'C3'}, #columns
    {'A1', 'B2', 'C3'}, {'A3', 'B2', 'C1'}, # diagonals
]

welcome_message = """
    WELCOME TO TIC TAC TOE!

    To play, enter the positions that you want you "X" to be placed.
         _1_ _2_ _3_
      A |___|___|___|
      B |___|___|___|
      C |___|___|___|

    For example, to place your "X" in the top left corner, type "A1".
    
    Whoever gets three in a row wins! You go first! 
    """

tie_message = "It is a tie! No one wins!"


def print_board(board):   
    """
    Summary of the function.

    Args:
        board(dict): Dictionary of each square on the board and its content.

    Returns:
        str: visual representation of the board in the console.

    Example:
        >>>     _1_ _2_ _3_
        >>> A |_O_|___|_X_|
        >>> B |___|_O_|_X_|
        >>> C |_O_|___|_X_|
    """
    print(f"""
               _1_ _2_ _3_
            A |_{board.get('A1','_')}_|_{board.get('A2','_')}_|_{board.get('A3','_')}_|
            B |_{board.get('B1','_')}_|_{board.get('B2','_')}_|_{board.get('B3','_')}_|
            C |_{board.get('C1','_')}_|_{board.get('C2','_')}_|_{board.get('C3','_')}_|
            """
    )
 
def find_open_position():
    open_positions = {key for key, value in board.items() if value == ' '}
    return open_positions

def insert_user_input():
    """
    Places an 'X' on the board at the user's chosen position.
    If the position is not valid, the user is prompted to try again with a list of possible positions.

    Args:
        None

    Returns:
        str: "X" is inserted into the board dictionary.
    """
    while True:
        open_positions = find_open_position()
        position = input('What is your move? ').upper()
        if position in open_positions:
            board[position] = 'X'
            print_board(board)
            break
        else:
            print(f"""
            {position} is not a valid position. Please try again.
            Possible positions: {open_positions}
            """)

def computer_input():
    """
    Chooses a random position on the board to place an 'O'.

    Args:
        None

    Returns:
        str: ")" is inserted into a random key in the board dictionary.
    """
    time.sleep(1) # pause for 1 second to simulate computer thinking
    open_positions = find_open_position()
    computer_input = random.choice(list(open_positions)) # sets can't be indexed, convert to list
    board[computer_input] = 'O'
    print(f'The computer chose {computer_input}')
    print_board(board)

def evaluate_winner(player_positions):
    """
    Evaluates whether a player has won the game.

    Args:
        player_positions(str): Positions of a given player.

    Returns:
        bool: True if any of the winning positions are a subset of the player's positions.
    """
    for position in range(len(winning_positions)):
        if winning_positions[position].issubset(player_positions):
            return True
    return False

def main():
    print(welcome_message)
    
    while True:
        insert_user_input()
        user_positions = {key for key, value in board.items() if value == 'X'}
        if evaluate_winner(user_positions) == True:
            print('CONGRATULATIONS! You win!')
        elif len(find_open_position()) == 0:
            print(tie_message)
            break

        computer_input()
        computer_positions ={key for key, value in board.items() if value == 'O'}
        if evaluate_winner(computer_positions) == True:
            print ('SORRY! The computer wins, Better luck next time!')
            break
        elif len(find_open_position()) == 0:
            print(tie_message)
            break

    print('Thanks for playing!')

main()


