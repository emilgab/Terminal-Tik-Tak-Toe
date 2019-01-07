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

# For testing purposes
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
