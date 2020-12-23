import random


def print_board_and_legend(board):  # Prints all moves that have been made along side a legend
    for i in range(3):
        line1 = " " + board[i][0] + " | " + board[i][1] + " | " + board[i][2]
        line2 = "  " + str(3 * i + 1) + " | " + str(3 * i + 2) + " | " + str(3 * i + 3)
        print(line1 + " " * 5 + line2)
        if i < 2:
            print("---+---+---" + " " * 5 + "---+---+---")


def make_empty_board():  # Creates an empty tic tac toe board
    board = []
    for i in range(3):
        board.append([" "] * 3)
    return board


def square_num(move): # converts a move (1-9) into a set of coordinates for the "board" list
    coordinates = [0, 0]
    row = ((move - 1) // 3)
    column = move - (row*3 + 1)
    coordinates[0] = row
    coordinates[1] = column
    return coordinates


def put_in_board(coordinates, board):  # takes the coordinate from square_num function and assigns it as the current move

    board[coordinates[0]][coordinates[1]] = move_counter()
    return board


def move_counter(): # keeps track of which move the game is on, if counter = 0, then X is played and vice versa
    global counter
    if counter == 0:
        counter = 1
        return 'X'
    else:
        counter = 0
        return 'O'


def check_square(move): # removes the previous move played from possible moves that can be made
    global possible_moves
    possible_moves.remove(move)
    return possible_moves


def rows_same(board):  # checks if any of the rows have the same game piece and if so returns a "true" win condition
    i = 0
    win_condition = 0
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            win_condition = 1
            return win_condition
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            win_condition = 1
            return win_condition
    return win_condition


def column_same(board):  # checks if any of the column have the same game piece and if so returns a "true" win condition
    i = 0

    win_condition = 0
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            win_condition = 1

        if board[0][i] == board[1][i] == board[2][i] == 'O':
            win_condition = 1

    return win_condition


def diagonal_same(board):  # checks if either diagonal have the same game piece and if so returns a "true" win condition
    i = 0

    win_condition = 0
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        win_condition = 1
        return win_condition
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        win_condition = 1
        return win_condition

    if board[0][0] == board[1][1] == board[2][2] == 'O':
        win_condition = 1
        return win_condition
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        win_condition = 1
        return win_condition
    return win_condition


def win_cond(board):  # checks if any of the win conditions have been met
    if (column_same(board) == 1) or (rows_same(board) == 1) or (diagonal_same(board) == 1):
        return 1
    else:
        return 0


def initialize(): # initialize the variables
    global counter, i, win_condition, move, possible_moves, board
    counter = 0
    i = 0
    win_condition = 0
    move = 0
    possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board = make_empty_board()
    print_board_and_legend(board)


def ai(board):
    # Takes in the possible moves that can be made, as well as the board and makes a copy of it(shallow copy)
    # The first if statement checks every available square to see if the computer would win if that move was played
    # second if statement determines if the human would win if that move was played and returns that coordinate to block
    # Lastly the copy of the board is reset to continue the loop
    # if it is not possible for either the human or computer to win, the a random move is made
    # computer winning is priority, then if human wins, then random choice
    global possible_moves
    i = 0
    new = []
    new = board.copy()
    priority = 0
    ai_win = 0
    human_win = 0
    for i in range(len(possible_moves)):
        row, column = square_num(possible_moves[i])
        new[row][column] = 'O'
        if win_cond(new) == 1:
            ai_win = possible_moves[i]
            priority = 1
            break
        new[row][column] = 'X'
        if win_cond(new) == 1:
            human_win = possible_moves[i]
            priority = 2
        new[row][column] = ' '
    if priority == 1:
        return ai_win
    if priority == 2:
        return human_win
    else:
        return random.choice(possible_moves)


def play_tic_tac_toe():  # function that executes the game
    initialize()

    while possible_moves:
        # human moves first, but this can be made by switching the input statement with the ai function
        if counter == 0:
            move = int(input("Make a move: "))
        if counter == 1:
            move = ai(board)
        # checks to make sure that the previous move played was valid
        # puts the move in the board and prints it along with the legend, then removes that square from possible moves
        if move in possible_moves:
            put_in_board(square_num(move), board)
            print_board_and_legend(board)
            check_square(move)
        else:
            print("INVALID MOVE")
        # checks to see if anybody won after the previously played move
        if win_cond(board) == 1:
            if counter == 1:
                print("X You Win")
                break
            if counter == 0:
                print("O You Win")
                break
    # once all possible moves have been made, if there are no winners, then the game is a tie
    if not possible_moves:
        print("Tie Game")


if __name__ == '__main__':
    play_tic_tac_toe()


