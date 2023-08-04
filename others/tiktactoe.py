import random as r
import os
import sys
import time
def print_board(mode,arr: list):
    os.system('clear')
    print('==========MODE===========')
    print('\n\tmode:'+mode)
    print('\n==========BOARD==========')
    print('\t\n-------------------------\n', end="|   ")
    for i in range(len(arr)):
        if i == 3 - 1 or i == 6 - 1:
            print(arr[i], end='   |   \n-------------------------\n|   ')
        else:
            print(arr[i], end='   |   ')
    print('\t\n-------------------------')
    print('\n========================\n')

def check_oc(board):
    for i in board:
        if isinstance(i, int):
            return False
    return True

def check_winner(board, move):
    winning_list = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]

    for combo in winning_list:
        if all(pos == move for pos in combo):
            return True

    return False

def play_again(mode):
    print('\n**OPTIONS**\n')
    print("[1]-----Play Again")
    print("[2]-----Menu")
    print('[3]------Exit')
    while True:
        try:
            ch = int(input('\nChoice:'))
        except:
            print('\nInvalid choice! Please enter 1, 2, or 3.')

        if ch == 1:
            os.system('clear')
            return vs_player(mode=mode, board=[1, 2, 3, 4, 5, 6, 7, 8, 9], occupied_slot=[], turn="X")
        elif ch == 2:
            os.system('clear')
            return main()
        elif ch == 3:
            print('\nGoodbye!')
            sys.exit()
        else:
            print('\nInvalid choice!')

def vs_player(mode='PLAYER', board=[1, 2, 3, 4, 5, 6, 7, 8, 9], occupied_slot=[], turn="X"):
    
    print_board(mode,board)

    if turn == 'X' or (turn == 'O' and mode == 'PLAYER') and mode !='BOT':
        while True:
            try:
                n = int(input(f"\n{turn}'s turn:")) - 1

                if n < 0 or n + 1 >= 10:
                    print('\nInvalid move')
                elif n in occupied_slot:
                    print('\nThe slot you entered was already occupied')
                else:
                    break
            except:
                print('\nInvalid input! Please choose a number from 1 to 9.')

    else:
        while True:
            bot_move = r.randint(1, 9)
            if bot_move in occupied_slot:
                continue
            else:
                n = bot_move - 1
                print(f"\n{turn}'s turn:{bot_move}")
                time.sleep(0.7)
                break

    occupied_slot.append(n)
    board[n] = turn

    isAllOccupied = check_oc(board)

    if isAllOccupied:
        os.system('clear')
        print_board(mode,board)
        print('\n==========RESULT=========\n')
        print('\n>>>> Tie <<<<')
        play_again(mode)

    win = check_winner(board, turn)
    if win:
        os.system('clear')
        print_board(mode,board)
        print('\n==========RESULT=========\n')
        print(f"\n>>>>> THE WINNER IS {turn} <<<<<\n")
        play_again(mode)

    if turn == 'X':
        turn = "O"
    else:
        turn = "X"

    return vs_player(mode, board, occupied_slot, turn)

def main():
    print('*** TIC TAC TOE ***')
    print("\n\n** GAME MODE **\n\n")
    print("[1]-----VS Player")
    print("[2]-----VS BOT")
    print('[3]-----Exit')
    while True:
        try:
            ch = int(input('\nMode:'))
        except:
            print('\nInvalid choice! Please enter 1, 2, or 3.')

        if ch == 1:
            vs_player(mode='PLAYER', board=[1, 2, 3, 4, 5, 6, 7, 8, 9], occupied_slot=[], turn="X")
            break
        elif ch == 2:
            vs_player(mode='BOT', board=[1, 2, 3, 4, 5, 6, 7, 8, 9], occupied_slot=[], turn="X")
            break
        elif ch == 3:
            print('\nGoodbye!')
            sys.exit()
        else:
            print('\nInvalid choice!')

if __name__ == '__main__':
    main()
