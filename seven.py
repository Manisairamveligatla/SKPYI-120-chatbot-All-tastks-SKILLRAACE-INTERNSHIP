import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    return O if countX > countO else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def check_winner(board, player):
    """
    Checks if the player has won on the board.
    """
    return (
        any(all(cell == player for cell in row) for row in board) or
        any(all(board[i][col] == player for i in range(3)) for col in range(3)) or
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2 - i] == player for i in range(3))
    )


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_winner(board, X):
        return X
    if check_winner(board, O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (win := winner(board)) == X:
        return 1
    if win == O:
        return -1
    return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        value, best_action = max((min_value(result(board, action)), action) for action in actions(board))
    else:
        value, best_action = min((max_value(result(board, action)), action) for action in actions(board))
    
    return best_action


# Test the implementation
if __name__ == "__main__":
    board = initial_state()
    print("Initial Board:")
    for row in board:
        print(row)
    
    while not terminal(board):
        current_move = minimax(board)
        board = result(board, current_move)
        for row in board:
            print(row)
        print()
    
    print("Final Board:")
    for row in board:
        print(row)
    print(f"Winner: {winner(board)}")
