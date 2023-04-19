def find_move(board, player):
    empty_moves = []
    capture_moves = []
    forced_capture_moves = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player:
                moves = get_valid_moves(board, player, row, col)
                for move in moves:
                    if is_capture_move(board, move):
                        capture_moves.append(move)
                        temp_board = [row[:] for row in board]
                        make_move(temp_board, player, move)
                        opponent_moves = get_all_valid_moves(temp_board, 3 - player)
                        forced_capture = all(is_capture_move(temp_board, m) for m in opponent_moves)
                        if forced_capture:
                            forced_capture_moves.append(move)
                    else:
                        empty_moves.append(move)

    capture_moves.sort(key=lambda move: move[1][0], reverse=(player == 1))
    empty_moves.sort(key=lambda move: (evaluate_move(board, player, move), move[1][0]), reverse=(player == 1))

    if forced_capture_moves:
        return forced_capture_moves[0]
    elif capture_moves:
        return capture_moves[0]
    elif empty_moves:
        return empty_moves[0]
    else:
        return None

def get_all_valid_moves(board, player):
    all_moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player:
                moves = get_valid_moves(board, player, row, col)
                all_moves.extend(moves)
    return all_moves

def make_move(board, player, move):
    start, end = move
    start_row, start_col = start
    end_row, end_col = end
    board[end_row][end_col] = player
    board[start_row][start_col] = 0

def get_valid_moves(board, player, row, col):
    direction = 1 if player == 1 else -1
    valid_moves = []

    if 0 <= row + direction < len(board) and board[row + direction][col] == 0:
        valid_moves.append(((row, col), (row + direction, col)))

    for dcol in [-1, 1]:
        if 0 <= col + dcol < len(board[row]) and 0 <= row + direction < len(board) and board[row + direction][col + dcol] == (3 - player):
            valid_moves.append(((row, col), (row + direction, col + dcol)))

    return valid_moves

def is_capture_move(board, move):
    start, end = move
    end_row, end_col = end
    return board[end_row][end_col] != 0

def evaluate_move(board, player, move):
    start, end = move
    start_row, start_col = start
    end_row, end_col = end

    # Center control
    central_bonus = 0
    if end_col in [2, 3]:
        central_bonus = 1

    # Diagonal protection
    protection_bonus = 0
    if (end_col - 1 >= 0 and board[end_row][end_col - 1] == player) or (end_col + 1 < len(board[end_row]) and board[end_row][end_col + 1] == player):
        protection_bonus = 1

    return central_bonus + protection_bonus
