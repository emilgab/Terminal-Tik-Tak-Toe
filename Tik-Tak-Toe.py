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
player1_marker, player2_marker = player_input()
player1_marker

# Function that takes in the board list object, a marker and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):

    board[position] = marker

# Testing to see that the place_marker() works as intended
# place_marker(test_board,'$',8)
# display_board(test_board)
