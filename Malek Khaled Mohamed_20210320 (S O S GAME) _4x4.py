# FCAI – Programming 1 – 2022 - Assignment 1
# Program Name: SOS GAME.py
# Program Description:
  # This game is called <SOS>
  # In short, the game depends on the presence of two players
  # each of whom takes turns playing, has the freedom to choose to play either <S> or <O> in the place he wants
  # and both players aim to form <SOS> horizontally, vertically or diagonally
  # and each time the player able to form <SOS> He has the right to play again
  # after all the blanks are filled, the times of forming <SOS> are calculated for each player
  # and who have largest number of times will be the winner, and if the number of times is equal, it will be a tie
  # <SOS> 4x4 Version

# Last Modification Date: 3/14/2022

import os

board = [["-", "-", "-", "-"], ["-", "-", "-", "-"], ["-", "-", "-", "-"], ["-", "-", "-", "-"]]


def play_board(board):
    print("\t\t |---------------------|")
    print("\t\t | " + board[0][0] + "  |  " + board[1][0] + "  |  " + board[2][0] + "  |  " + board[3][0] + " |")
    print("\t\t |---------------------|")
    print("\t\t | " + board[0][1] + "  |  " + board[1][1] + "  |  " + board[2][1] + "  |  " + board[3][1] + " |")
    print("\t\t |---------------------|")
    print("\t\t | " + board[0][2] + "  |  " + board[1][2] + "  |  " + board[2][2] + "  |  " + board[3][2] + " |")
    print("\t\t |---------------------|")
    print("\t\t | " + board[0][3] + "  |  " + board[1][3] + "  |  " + board[2][3] + "  |  " + board[3][3] + " |")
    print("\t\t |---------------------|")


def take_player1_input(board):

    while True:
        while True:

            player1_row_play = input(" << Player1 : Enter a number 1 : 4 for row >> --> ")
            player1_column_play = input(" << Player1 : Enter a number 1 : 4 for column >> --> ")
            print("")
            if player1_row_play.isdigit() and player1_column_play.isdigit():
                break
            else:
                print("<< Please Enter numbers only >>")

        player1_row_play = int(player1_row_play)
        player1_column_play = int(player1_column_play)

        if player1_row_play >= 1 and player1_row_play <= 4 \
                and player1_column_play >= 1 and player1_column_play <= 4 \
                and board[player1_column_play - 1][player1_row_play - 1] == "-":
            while True:
                board[player1_column_play - 1][player1_row_play - 1] = (input(" << Choose < S > or < O >!  >> :  ")).upper()
                if board[player1_column_play - 1][player1_row_play - 1] == "S" \
                        or board[player1_column_play - 1][player1_row_play - 1] == "O":
                    wins = player_check_win(player1_column_play, player1_row_play, board)
                    if wins > 0:
                        count_player1 = 0
                        count_player1 += wins
                        return count_player1, wins
                    else:
                        return 0, 0
                    break
                else:

                    print("<< Please enter < S > or < O > only >>")
                    print("")
            break
        else:

            print("<< This place was taken or not defined try again >>")
            print("")


def take_player2_input(board):
    while True:
        while True:

            player2_row_play = input(" << Player2 : Enter a number 1 : 4 for row >> --> ")
            player2_column_play = input(" << Player2 : Enter a number 1 : 4 for column >> --> ")
            print("")
            if player2_row_play.isdigit() and player2_column_play.isdigit():
                break
            else:
                print("<< Please Enter number only >>")

        player2_row_play = int(player2_row_play)
        player2_column_play = int(player2_column_play)

        if player2_row_play >= 1 and player2_row_play <= 4 \
                and player2_column_play >= 1 and player2_column_play <= 4 \
                and board[player2_column_play - 1][player2_row_play - 1] == "-":
            while True:
                board[player2_column_play - 1][player2_row_play - 1] = (input(" << Choose < S > or < O >! >> :  ")).upper()
                if board[player2_column_play - 1][player2_row_play - 1] == "S" \
                        or board[player2_column_play - 1][player2_row_play - 1] == "O":
                    wins = player_check_win(player2_column_play, player2_row_play, board)
                    if wins > 0:
                        count_player2 = 0
                        count_player2 += wins
                        return count_player2, wins
                    else:
                        return 0, 0
                    break
                else:

                    print("<< Please enter < S > or < O > >>")
                    print("")
            break
        else:

            print("<< This place was taken or not defined try again >>")
            print("")


def player_check_win(player_column_play, player_row_play, board):
    count = 0
    if (player_column_play - 1) - 2 >= 0:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[(player_column_play - 1) - 1][player_row_play - 1] == "O" \
                and board[(player_column_play - 1) - 2][player_row_play - 1] == "S":
            count += 1

    if (player_column_play - 1) + 2 <= 3:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[(player_column_play - 1) + 1][player_row_play - 1] == "O" \
                and board[(player_column_play - 1) + 2][player_row_play - 1] == "S":
            count += 1

    if (player_column_play - 1) + 1 <= 3 and (player_column_play - 1) - 1 >= 0:
        if board[player_column_play - 1][player_row_play - 1] == "O" \
                and board[(player_column_play - 1) - 1][player_row_play - 1] == "S" \
                and board[(player_column_play - 1) + 1][player_row_play - 1] == "S":
            count += 1

    if (player_row_play - 1) - 2 >= 0:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[player_column_play - 1][(player_row_play - 1) - 1] == "O" \
                and board[player_column_play - 1][(player_row_play - 1) - 2] == "S":
            count += 1

    if (player_row_play - 1) + 2 <= 3:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[player_column_play - 1][(player_row_play - 1) + 1] == "O" \
                and board[player_column_play - 1][(player_row_play - 1) + 2] == "S":
            count += 1

    if (player_row_play - 1) + 1 <= 3 and (player_row_play - 1) - 1 >= 0:
        if board[player_column_play - 1][player_row_play - 1] == "O" \
                and board[player_column_play - 1][(player_row_play - 1) - 1] == "S" \
                and board[player_column_play - 1][(player_row_play - 1) + 1] == "S":
            count += 1

    if (player_column_play - 1) - 2 >= 0 and (player_row_play - 1) - 2 >= 0:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[(player_column_play - 1) - 1][(player_row_play - 1) - 1] == "O" \
                and board[(player_column_play - 1) - 2][(player_row_play - 1) - 2] == "S":
            count += 1

    if (player_column_play - 1) + 2 <= 3 and (player_row_play - 1) + 2 <= 3:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[(player_column_play - 1) + 1][(player_row_play - 1) + 1] == "O" \
                and board[(player_column_play - 1) + 2][(player_row_play - 1) + 2] == "S":
            count += 1

    if (player_column_play - 1) - 1 >= 0 and (player_row_play - 1) - 1 >= 0 \
            and (player_column_play - 1) + 1 <= 3 and (player_row_play - 1) + 1 <= 3:
        if board[player_column_play - 1][player_row_play - 1] == "O" \
                and board[(player_column_play - 1) - 1][(player_row_play - 1) - 1] == "S" \
                and board[(player_column_play - 1) + 1][(player_row_play - 1) + 1] == "S":
            count += 1

    if (player_column_play - 1) + 2 <= 3 and (player_row_play - 1) - 2 >= 0:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[(player_column_play - 1) + 1][(player_row_play - 1) - 1] == "O" \
                and board[(player_column_play - 1) + 2][(player_row_play - 1) - 2] == "S":
            count += 1

    if (player_column_play - 1) - 2 >= 0 and (player_row_play - 1) + 2 <= 3:
        if board[player_column_play - 1][player_row_play - 1] == "S" \
                and board[(player_column_play - 1) - 1][(player_row_play - 1) + 1] == "O" \
                and board[(player_column_play - 1) - 2][(player_row_play - 1) + 2] == "S":
            count += 1

    if (player_column_play - 1) + 1 <= 3 and (player_row_play - 1) - 1 >= 0 \
            and (player_column_play - 1) - 1 >= 0 and (player_row_play - 1) + 1 <= 3:
        if board[player_column_play - 1][player_row_play - 1] == "O" \
                and board[(player_column_play - 1) + 1][(player_row_play - 1) - 1] == "S" \
                and board[(player_column_play - 1) - 1][(player_row_play - 1) + 1] == "S":
            count += 1
    return count


def result_board():
    print("")
    print("\t  |-----------------------------------|")
    print("\t||         player 1 : player 2 \t       ||")
    print("     *|||             ------------- \t        |||*")
    print("\t||              ", count_player1, " : ", count_player2, "\t       ||")
    print("\t  |-----------------------------------|")
    print("")


def place_full_check(board):
    count = 0
    for column in board:
        for place in column:
            if place == "-":
                count += 1
    if count == 0:
        return True


def restart_game(board):
    for column in board:
        for place in range(4):
            column[place] = "-"


while True:

    count_player1 = 0
    count_player2 = 0
    result_board()
    play_board(board)
    print("")

    while True:

        while True:

            count1, win1 = take_player1_input(board)
            count_player1 += count1
            result_board()
            play_board(board)
            print("")
            if win1 == 0 or place_full_check(board) == True:
                break
            print(" << Oh this is win! play again >>")

        if place_full_check(board) == True:
            if count_player1 > count_player2:
                print("<< ------------ << PLAYER <1> IS WINNER >> ------------ >>")
                print("")
                play_board(board)
                break
            elif count_player2 > count_player1:
                print("<< ------------ << PLAYER <2> IS WINNER >> ------------ >>")
                print("")
                play_board(board)
                break
            elif count_player1 == count_player2:
                print("<< --------------------- << DRAW >> --------------------- >>")
                print("")
                play_board(board)
                break

        while True:

            count2, win2 = take_player2_input(board)
            count_player2 += count2
            result_board()
            play_board(board)
            print("")
            if win2 == 0 or place_full_check(board) == True:
                break
            print(" << Oh this is win! play again >>")

        if place_full_check(board) == True:
            if count_player1 > count_player2:
                print("<< ------------ << PLAYER <1> IS WINNER >> ------------ >>")
                print("")
                play_board(board)
                break
            elif count_player2 > count_player1:
                print("<< ------------ << PLAYER <2> IS WINNER >> ------------ >>")
                print("")
                play_board(board)
                break
            elif count_player1 == count_player2:
                print("<< -------------------- << DRAW >> --------------------0 >>")
                print("")
                play_board(board)
                break

    while True:
        print("")
        play_again = (input("<< Want to play again ? , (y/n) >> ")).lower()

        if play_again == "y" or play_again == "n":
            break
        else:
            print("<< Answer with (y/n) only >>")
            print("")

    if play_again == "y":
        os.system('CLS')
        restart_game(board)

    elif play_again == "n":
        print("")
        print(" <<-------<< GAME END >>------- >>")
        print("")
        game_end = input(" << Please press <Enter> to close the Game >>")
        break