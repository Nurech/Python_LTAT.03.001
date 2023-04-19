def read_settings():
    global central_bonus, protection_bonus, capturing_bonus, mobility_bonus, potential_capture_bonus, exposure_penalty, aggressive_capture_bonus

central_bonus = 3
protection_bonus = 8
capturing_bonus = 8
mobility_bonus = 2
potential_capture_bonus = 6
exposure_penalty = 10
aggressive_capture_bonus = 1

try:
    with open("settings.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split('=')
            if key == "central_bonus":
                central_bonus = int(value)
            elif key == "protection_bonus":
                protection_bonus = int(value)
            elif key == "capturing_bonus":
                capturing_bonus = int(value)
            elif key == "mobility_bonus":
                mobility_bonus = int(value)
            elif key == "potential_capture_bonus":
                potential_capture_bonus = int(value)
            elif key == "exposure_penalty":
                exposure_penalty = int(value)
            elif key == "aggressive_capture_bonus":
                aggressive_capture_bonus = int(value)
except FileNotFoundError:
    print("Settings file not found. Using default values.")


def find_move(board, player):
    empty_moves = []
    capture_moves = []
    forced_capture_moves = []
    corner_moves = []

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
                        if move[1] == (0, 3) and player == 1 or move[1] == (3, 0) and player == 2:
                            corner_moves.append(move)

    capture_moves.sort(key=lambda move: move[1][0], reverse=(player == 1))
    empty_moves.sort(key=lambda move: (evaluate_move(board, player, move), move[1][0]), reverse=(player == 1))
    corner_moves.sort(key=lambda move: move[1][0], reverse=(player == 1))

    if forced_capture_moves:
        return forced_capture_moves[0]
    elif capture_moves:
        return capture_moves[0]
    elif corner_moves:
        return corner_moves[0]
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
    a = 0
    if end_col in [1, 2]:
        a = central_bonus

    # Diagonal protection
    b = 0
    if (end_col - 1 >= 0 and board[end_row][end_col - 1] == player) or (
            end_col + 1 < len(board[end_row]) and board[end_row][end_col + 1] == player):
        b = 3

    # Capturing bonus
    d = 0
    if is_capture_move(board, move):
        d = capturing_bonus

    # Exposure penalty
    e = 0
    temp_board = [row[:] for row in board]
    make_move(temp_board, player, move)
    opponent_moves = get_all_valid_moves(temp_board, 3 - player)
    if any(is_capture_move(temp_board, m) and m[1] == end for m in opponent_moves):
        e = exposure_penalty

    # Aggressive capture bonus
    f = 0
    temp_board = [row[:] for row in board]
    make_move(temp_board, player, move)
    opponent_pieces = sum(1 for row in temp_board for cell in row if cell == 3 - player)
    if opponent_pieces <= 2:
        f = aggressive_capture_bonus

    # Mobility
    temp_board = [row[:] for row in board]
    make_move(temp_board, player, move)
    g = mobility_bonus * len(get_all_valid_moves(temp_board, player))

    # Potential captures
    potential_captures = sum(1 for m in get_all_valid_moves(temp_board, player) if is_capture_move(temp_board, m))
    h = potential_capture_bonus * potential_captures * 2

    return a + b + d - e + f + g + h
