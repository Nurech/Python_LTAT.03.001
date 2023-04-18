import json


def find_move(board, player):

    # If no good move is found from sims, use regular logic
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player:
                moves = get_valid_moves(board, player, row, col)
                if moves:
                    return moves[0]

def get_valid_moves(board, player, row, col):
    direction = 1 if player == 1 else -1
    valid_moves = []

    if 0 <= row + direction < len(board) and board[row + direction][col] == 0:
        valid_moves.append(((row, col), (row + direction, col)))

    for dcol in [-1, 1]:
        if 0 <= col + dcol < len(board[row]) and 0 <= row + direction < len(board) and board[row + direction][col + dcol] == (3 - player):
            valid_moves.append(((row, col), (row + direction, col + dcol)))

    return valid_moves
