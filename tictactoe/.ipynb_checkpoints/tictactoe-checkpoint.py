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
    movimiento_x = 0
    movimiento_o = 0
    
    for row in board:
        for dato in row:
            if dato == "X":
                movimiento_x += 1
                
            if dato == "O":  
                movimiento_o += 1

    if movimiento_x > movimiento_o: return "O"
    if movimiento_x == movimiento_o: return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """ 
    ## Posiblemente no se use next_player  = player(board)
    posibilidades = set()
    i = 0
    
    for row in board:
        j = 0
        for dato in row:
            if dato == EMPTY:
                posibilidades.add((i,j)) 
            j += 1
        i += 1        
    return posibilidades


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy
    resultado = copy.deepcopy(board)
    indice = 0
    accion_player = player(resultado)
    i = action[0]
    j = action[1]

    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("Casilla Ocupada")

    if resultado[i][j] is not None:
        raise ValueError("Casilla ya Ocupada")
    
    for row in resultado:
        subindice = 0
        for dato in row:
            if indice == i and subindice == j:
                resultado[indice][subindice] = accion_player
            subindice += 1
        indice += 1
            
    return resultado

            
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_X = ["X", "X", "X"]
    winner_O = ["O", "O", "O"]
    lector_columnas = [[],[],[]]
    cross_constructor = [[],[]]
    ganador = "NaN"
    i = 0
    
    for row in board:
        lector_filas = []
        j = 0
        for dato in row:
            lector_filas.append(dato)
            lector_columnas[j].append(dato)
            if i == j: 
                cross_constructor[0].append(dato)
            if i ==2 - j: 
                cross_constructor[1].append(dato)
            j += 1
        i += 1
        if lector_filas == winner_X: return "X"
        if lector_filas == winner_O: return "O"

    for j in range(3):
        if lector_columnas[j] == winner_X: return "X"
        if lector_columnas[j] == winner_O: return "O"

    if cross_constructor[0] == winner_X: return "X"
    if cross_constructor[0] == winner_O: return "O"
    if cross_constructor[1] == winner_X: return "X"
    if cross_constructor[1] == winner_O: return "O"

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_winner = winner(board)
    
    if is_winner is not None: return True
    else:
        for row in board:
            for dato in row:
                if dato == EMPTY: return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    who_wins = winner(board)
    if who_wins == "X" : return 1
    if who_wins == "O" : return -1
    
    
    return 0


def minimax(board, is_root_call=True):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None if is_root_call else utility(board)
        
    who_is_player = player(board)
    mejor_accion = None
    ## deep = 6 Podemos optimizar reduciendo el deep de posibilidades
    if who_is_player == "X":
        v = -float("inf")

        for accion in actions(board):
            new_board = result(board, accion)
            new_value = minimax(new_board, is_root_call=False)
            if new_value is not None and new_value > v:
                v = new_value
                mejor_accion = accion
        return mejor_accion if is_root_call else v

    else:
        v = float("inf")
        for accion in actions(board):
            new_board = result(board, accion)
            new_value = minimax(new_board, is_root_call=False)  
            if new_value is not None and new_value < v:
                v = new_value  
                mejor_accion = accion  

        return mejor_accion if is_root_call else v
