# For Jupyter Notebook
from IPython.display import clear_output

# Creates the board for tik tak toe
def display_board(board):

    # Method only working in Jupyter Notebook
    # clear_output()
    # Work-around for running the script other than in Jupyter
    print ('\n'*100)

    # Printing the display_board
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-   -   -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-   -   -')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

# For testing purposes. To check how the board would look
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''

    # Keep asking player 1 to choose X or O with a while loop

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    # Assign Player 2 to the opposite marker
    # The markers are stored in tuples which we can tuple unpack later
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

# Testing user input
# player1_marker, player2_marker = player_input()
# player1_marker

# Function that takes in the board list object, a marker and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):

    board[position] = marker

# Testing to see that the place_marker() works as intended
# place_marker(test_board,'$',8)

# Writting a function that takes in a board and a mark (X or O) and then checks to see if that mark has won!
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Testing win_check(), should return True
# win_check(test_board,'X')

# Function that uses the random module to decide which player goes first

import random

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Function that returns True/False infication whether a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    # Board is full if we return True
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))

    return position

# Function that asks the player if they want to play again and returns a boolean True if they do want to play again
def replay():
    choice = input("Play again? Enter Yes or No")

    return choice == "Yes"

# While loop to keep running the game
print("Welcome to Tic Tac Toe!")

while True:
    # Play the game
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")


    play_game = input("Ready to play? y or n?")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position that they chose
            place_marker(the_board,player1_marker,position)
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    break
                else:
                    turn = 'Player 2'

        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position that they chose
            place_marker(the_board,player2_marker,position)
            # Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
    # Break out of the while loop
