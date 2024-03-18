"""
Tic Tac Toe Player
"""

import math

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

    # Count X's and O's on board
    count_X = 0
    count_O = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_X += 1
            elif cell == O:
                count_O += 1
    
    # if there's more X's than O's, it's O's turn
    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # The set of all possible actions is the set of all empty cells
    actions = set()

    # Loop through all cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if action is valid
    if action not in actions(board):
        raise Exception("Invalid Action")
    
    # Copy the board
    new_board = [row.copy() for row in board]

    # Get the current player
    current_player = player(board)

    # Make the move
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
        
    # Check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
            
    # Check diagonals
            if board[0][0] == board[1][1] == board[2][2]:
                return board[0][0]
            if board[0][2] == board[1][1] == board[2][0]:
                return board[0][2]
            
    return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # if there's a winner game = over
    if winner(board) is not None:
        return True
    
    # if there's empty cells, game = not over
    for row in board:
        if EMPTY in row:
            return False
        
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    #Get Winner
    win = winner(board)

    #return utility X = +1, O = -1, Draw = 0
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Get the current player
    current_player = player(board)

    # If the board is terminal, the game is over
    if terminal(board):
        return None

    # If the current player is X
    if current_player == X:
        v = -math.inf
        # Initialize best action to None to assign it later
        best_action = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_action = action
        return best_action

    # If the current player is O
    else:
        v = math.inf
        # Initialize best action to None to assign it later
        best_action = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        return best_action
    


def max_value(board):
    """
    Returns the maximum utility value for the current player
    """

    # If the board is terminal, return the utility value
    if terminal(board):
        return utility(board)

    # Initialize v to negative infinity
    v = -math.inf
    # Loop through all possible actions
    for action in actions(board):
        # Get the maximum value of the minimum values of the next player
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Returns the minimum utility value for the current player
    """

    # If the board is terminal, return the utility value
    if terminal(board):
        return utility(board)

    # Initialize v to positive infinity
    v = math.inf
    # Loop through all possible actions
    for action in actions(board):
        # Get the minimum value of the maximum values of the next player
        v = min(v, max_value(result(board, action)))
    return v


