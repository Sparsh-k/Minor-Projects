def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])
test_board=['']*10

def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input("Player 1 choose between X or O: ").upper()
        break
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    print(f'player1: {player1}')
    print(f'player2: {player2}')
    return(player1,player2)

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,marker):
    # print(((board[7] == board[8] == board[9] == marker) or
    # (board[4] == board[5] == board[6] == marker) or
    # (board[1] == board[2] == board[3] == marker) or
    # (board[7] == board[4] == board[1] == marker) or
    # (board[8] == board[5] == board[2] == marker) or
    # (board[9] == board[6] == board[3] == marker) or
    # (board[7] == board[5] == board[3] == marker) or
    # (board[1] == board[5] == board[9] == marker)))
    # ROWS
    return ((board[7] == board[8] == board[9] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[1] == board[2] == board[3] == marker) or
    # COLUMNS
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    # CROSS
    (board[7] == board[5] == board[3] == marker) or
    (board[1] == board[5] == board[9] == marker))

import random

def choose_first():
    flip=random.randint(0,1)
    if flip==1:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board,postiion):
    return board[postiion]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a position from 1-9:"))
        break
    return position

def replay():
    choice=input("Do you want to play again? Yes or No: ").upper()
    return choice=='YES'

##########################################################################################################################
## Game logic from here
print('Welcome To Tic Tac Toe')
the_board=[' ']*10
player1_marker,player2_marker=player_input()
turn=choose_first()
print(turn + 'Will go first')
play_game=input("Ready to Play? Y or N: ").upper()
if play_game=='Y':
    game_on=True
else:
    game_on=False
while True:
    while game_on:
        if turn == 'player 1':

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 WON THE GAME")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S TIE")
                    game_on=False
                else:
                    turn = 'player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 WON THE GAME")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("IT'S TIE")
                    game_on = False
                else:
                    turn = 'player 1'
    if not replay():
        break