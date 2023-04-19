import itertools


def generate_moves(board, player):
    moves = []
    for r, c in itertools.product(range(len(board)), range(len(board[0]))):
        if board[r][c] == player:
            for dr, dc in [(1, 0), (1, 1), (1, -1)] if player == 1 else [(-1, 0), (-1, 1), (-1, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != player:
                    moves.append(((r, c), (nr, nc)))
    return moves


def apply_move(board, move):
    new_board = [row.copy() for row in board]
    src, dest = move
    new_board[src[0]][src[1]] = 0
    new_board[dest[0]][dest[1]] = board[src[0]][src[1]]
    return new_board


def find_move(board, player, config=None):
    if config is None:
        config = {
            "grouping_weight": 2,
            "capture_weight": 2,
            "center_weight": 2,
            "fork_weight": 2,
            "defense_weight": 2,
            "objective_weight": 2,
            "block_fork_weight": 2,
            "safe_move_weight": 2,
            "edge_weight": 2,
            "corner_weight": 2,
            "avoid_opportunity_weight": 2,
        }

    best_move = None
    best_score = float('-inf')

    for move in generate_moves(board, player):
        new_board = apply_move(board, move)
        score = evaluate_move(new_board, player, move, config)
        if score > best_score:
            best_move = move
            best_score = score

    return best_move


def evaluate_move(board, player, move, config):
    opponent = 3 - player
    if is_winning_move(board, player, move):
        return float('inf')

    score = 0
    if is_grouping_move(board, player, move):
        score += config["grouping_weight"]

    if is_capturing_move(move) and not is_winning_move(board, opponent, move):
        score += config["capture_weight"]

    if is_center_move(move):
        score += config["center_weight"]

    if is_fork_move(board, player, move):
        score += config["fork_weight"]

    if is_defensive_move(board, player, move):
        score += config["defense_weight"]

    score += config["objective_weight"] * (move[1][0] if player == 1 else len(board) - move[1][0] - 1)

    if is_blocking_enemy_fork_move(board, player, move):
        score += config["block_fork_weight"]

    if is_safe_move(board, player, move):
        score += config["safe_move_weight"]

    if is_edge_move(board, move):
        score += config["edge_weight"]

    if is_corner_move(board, move):
        score += config["corner_weight"]

    if not is_opponent_opportunity_move(board, player, move):
        score += config["avoid_opportunity_weight"]

    return score


def is_grouping_move(board, player, move):
    _, dest = move
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = dest[0] + dr, dest[1] + dc
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == player:
            return True
    return False


def is_blocking_enemy_fork_move(board, player, move):
    new_board = apply_move(board, move)
    opponent_moves = generate_moves(new_board, 3 - player)
    return not any(is_fork_move(new_board, 3 - player, opp_move) for opp_move in opponent_moves)


def is_safe_move(board, player, move):
    new_board = apply_move(board, move)
    opponent_moves = generate_moves(new_board, 3 - player)
    return not any(is_capturing_move(opp_move) and opp_move[1] == move[1] for opp_move in opponent_moves)


def is_center_move(move):
    _, dest = move
    return dest == (1, 1) or dest == (1, 2) or dest == (2, 1) or dest == (2, 2)


def is_fork_move(board, player, move):
    new_board = apply_move(board, move)
    opponent_moves = generate_moves(new_board, 3 - player)
    return sum(1 for opp_move in opponent_moves if is_capturing_move(opp_move)) >= 2


def is_defensive_move(board, player, move):
    new_board = apply_move(board, move)
    opponent_moves = generate_moves(new_board, 3 - player)
    return any(is_capturing_move(opp_move) for opp_move in opponent_moves)


def is_winning_move(board, player, move):
    _, dest = move
    return dest[0] == len(board) - 1 if player == 1 else dest[0] == 0


def is_capturing_move(move):
    src, dest = move
    return abs(src[1] - dest[1]) == 1


def is_edge_move(board, move):
    _, dest = move
    return dest[0] in (0, len(board) - 1) or dest[1] in (0, len(board[0]) - 1)


def is_corner_move(board, move):
    r, c = move[1]
    return (r, c) in [(0, 0), (0, len(board[0]) - 1), (len(board) - 1, 0), (len(board) - 1, len(board[0]) - 1)]


def is_opponent_opportunity_move(board, player, move):
    new_board = apply_move(board, move)
    opponent_moves = generate_moves(new_board, 3 - player)
    return any(is_capturing_move(opp_move) or is_fork_move(new_board, 3 - player, opp_move) for opp_move in opponent_moves)
