import octopawn
import random

BOARD_SIZE = 4

class InvalidMove(Exception):
    pass

def init_board():
    return [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 2]]

def print_board(board):
    print("\n".join([" ".join([str(el) for el in row]) for row in board]), end="\n\n")

def possible_moves(board, player):
    moves = set()
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            
            pl = board[x][y]
            
            if pl == player == 1:
                fw = 1
            elif pl == player == 2:
                fw = -1
            else:
                continue
            
            other = 3 - pl

            if x + fw < BOARD_SIZE and x + fw >= 0:
                
                # Move forward
                if board[x + fw][y] == 0:
                    moves.add(((x, y), (x + fw, y)))

                # Take left
                if y - 1 >= 0 and board[x + fw][y - 1] == other:
                    moves.add(((x, y), (x + fw, y - 1)))
                
                # Take right
                if y + 1 < BOARD_SIZE and board[x + fw][y + 1] == other:
                    moves.add(((x, y), (x + fw, y + 1)))
    return moves

def find_move(board, player):
    s = possible_moves(board, player)

    if len(s) == 0:
        raise InvalidMove(board, player)

    return random.sample(list(s), 1)[0]

def make_move(board, move):
    x0, y0 = move[0]
    x1, y1 = move[1]
    board[x1][y1] = board[x0][y0]
    board[x0][y0] = 0
    return board

def check_win(board, player):
    for y in range(BOARD_SIZE):
        if board[BOARD_SIZE - 1][y] == 1:
            return 1
        if board[0][y] == 2:
            return 2
    if len(possible_moves(board, player)) == 0:
        return 3 - player
    return 0

def play(player=1):
    board = init_board()
    print_board(board)

    while check_win(board, player) == 0:
        if player == 1:
            move = octopawn.find_move(board, player)
        else: 
            move = find_move(board, player)
        
        make_move(board, move)
        print("Player", player, "moved:")
        print_board(board)

        player = 3 - player
        
    print("Player", check_win(board, player), "won")

play()