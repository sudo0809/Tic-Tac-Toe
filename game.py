

def display_board(board):
    blankboard = """
    ___________________
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  5  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  1  |  2  |  3  |
    |     |     |     |
    |-----------------|
    """
    for i in range(1, 10):
        if (board[i-1] == 'O' or board[i-1] == "X"):
            blankboard = blankboard.replace(str(i), board[i-1])
        else:
            blankboard = blankboard.replace(str(i), " ")

    print(blankboard)


def player_input():
    player1 = input("Pick a marker from 'X' or 'O' ")
    while True:
        if player1.upper() == "O":
            player2 = "X"
            return player1.upper(), player2
        elif player1.upper() == "X":
            player2 = "O"
            return player1.upper(), player2
        else:
            print("Invalid marker. Please choose again!!")
            player1 = input("Pick a marker from 'X' or 'O' ")


def get_markers():
    player1marker, player2marker = player_input()
    print("Player 1 choose", player1marker, "marker")
    print("So Player 2 gets", player2marker, "marker")


def place_marker(board, marker, position):
    board[position-1] = marker
    return board


def blank_space_in_board(position, board):
    return board[position-1] == "#"


def player_choice(board):
    choice = input("Please select an empty space from position 1 to 9: ")
    while not blank_space_in_board(int(choice), board):
        choice = input(
            "This is not an empty space. Please select again from 1 to 9: ")
    return choice


def check_full_filled(board):
    for i in board:
        if i == "#":
            return False
    return True


def check_win(board, marker):
    # row wise check
    for row in range(0, 3):
        if board[row] == board[row+3] == board[row+6] == marker:
            return True
    # col wise check
    for col in [0, 3, 6]:
        if board[col] == board[col+1] == board[col+2] == marker:
            return True

    # diagonally check
    if board[0] == board[4] == board[8] == marker:
        return True

    if board[6] == board[4] == board[2] == marker:
        return True

    return False


def replay():
    play = input("Press 'y' to play again and 'n' to exit : ")
    if play.lower() == 'y':
        return True
    if play.lower() == 'n':
        return False


def game():
    print("Welcome to Tic-Tac-Toe")

    # ḷets take the players input
    P1, P2 = player_input()
    # suppose P1='X' and P2='O'

    board = ['#']*9
    # makes an empty board

    i = 1
    # keep track of the players turn

    while True:

        while not check_full_filled(board):
            # player choses the position to place its marker
            position = player_choice(board)

            # whose turn is it
            if i % 2 == 0:
                marker = P2
            else:
                marker = P1

            place_marker(board, marker, int(position))

            display_board(board)

            i += 1

            if check_win(board, marker):
                print("You Won!!")
                break

        if check_win(board, marker):
            print("You Won!!")

        if replay():
            i = 1
            board = ["#"]*9
            P1, P2 = player_input()
        else:
            break


if __name__ == "__main__":

    game()
