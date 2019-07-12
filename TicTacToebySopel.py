import itertools
 
SYMBOL_NONE = ' '
SYMBOL_O = 'O'
SYMBOL_X = 'X'
 
WIN_DIAGONAL_MAIN = 0
WIN_DIAGONAL_REVERSED = 1
WIN_HORIZONTAL = 2
WIN_VERTICAL = 3
 
win_messages = {
    WIN_DIAGONAL_MAIN : "player {} is the winner diagonally (\\)!",
    WIN_DIAGONAL_REVERSED : "player {} is the winner diagonally (/)!",
    WIN_HORIZONTAL : "player {} is the winner horizontally!",
    WIN_VERTICAL : "Player {} is the winner vertically (|)!"
}
 
stalemate_message = "Stalemate! It's a tie."
 
def is_winning_sequence(l):
    if l.count(l[0]) == len(l) and l[0] != SYMBOL_NONE:
        return True
    else:
        return False
 
def winner_by_main_diagonal(board):
    cells = []
    for col, row in enumerate(reversed(range(len(board)))):
        cells.append(board[row][col])
 
    if is_winning_sequence(cells):
        print()
        return cells[0]
    return None
 
def winner_by_reversed_diagonal(board):
    cells = []
    for ix in range(len(board)):
        cells.append(board[ix][ix])
    if is_winning_sequence(cells):
        return cells[0]
    return None
 
def winner_by_rows(board):
    # horizontal
    for row in board:
        if is_winning_sequence(row):
            return row[0]
 
    return None
 
def winner_by_columns(board):
    for col in range(len(board)):
        cells = []
 
        for row in board:
            cells.append(row[col])
 
        if is_winning_sequence(cells):
            return cells[0]
 
    return None
 
def is_filled(board):
    for row in board:
        for col in row:
            if col == SYMBOL_NONE:
                return False
 
    return True
 
win_checks = [
    (winner_by_main_diagonal, WIN_DIAGONAL_MAIN),
    (winner_by_reversed_diagonal, WIN_DIAGONAL_REVERSED),
    (winner_by_rows, WIN_HORIZONTAL),
    (winner_by_columns, WIN_VERTICAL)
]
 
def classify_win(board):
    for (f, t) in win_checks:
        w = f(board)
        if w:
            return t, w
    return None
 
def print_board(board):
    print("   "+"  ".join([str(i) for i in range(len(board))]))
 
def place_symbol(board, player, row, column):
    try:
        if board[row][column] != SYMBOL_NONE:
            print("this position is occupado! choose another!")
            return False
        print_board(board)
        board[row][column] = player
        for count, row in enumerate(board):
            print(count, row)
        return True
 
    except IndexError as e:
        print("select row/column as 0 1 or 2", e)
        return False
 
    except Exception as e:
        print("something went wrong", e)
        return False
 
play = True
players = [1, 2]
while play:
    board = [[SYMBOL_NONE for i in range(3)] for i in range(3)]
    game_won = False
    print_board(board)
    player_choice = itertools.cycle([SYMBOL_O, SYMBOL_X])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        while not played:
            column_choice = int(input("what column do you want to play? (0, 1, 2): "))
            row_choice = int(input("what row do you want to play? (0, 1, 2): "))
            played = place_symbol(board, current_player, row_choice, column_choice)
 
        w = classify_win(board)
        if w:
            game_won = True
            type, winner = w
            print(win_messages[type].format(winner))
            again = input("The game is over, would you like to play again? y/n) ")
            if again.lower() == "y":
                print("restarting game")
            elif again.lower() == "n":
                print("Thanks for play, bye")
                play = False
            else:
                print("Thanks for play, bye")
                play = False
        elif is_filled(board):
            print(stalemate_message)
            play = False
