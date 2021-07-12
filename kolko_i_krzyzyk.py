import os
import random

# os - biblioteka umożliwiająca komunikacje z systemem

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')


# nt - na widnows else dla systemów unixowych (mac, linux)
def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# pierwszy indeks listy to zero, gdy printujesz board 1 to masz 2 pozycje w liście
#display_board(test_board)


def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1,choose X or O: ').upper()

    if marker == 'X':

        return ('X', 'O')
    else:
        return ('O', 'X')


#player1_marker, player2_marker = player_input()


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    # win Tic Tac Toe?

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
        # Board is full if we return True
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position


def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'


# While Loop to Keep Running the game
print('Welcome to Tic Tac Toe')
while True:
    # Play the game
    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? y or n? ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    ## GAME PLAY
    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)
            # check if then won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)
            # check if then won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
# All columns, check to see if marker matches
# 2 diagonals, check to see match
