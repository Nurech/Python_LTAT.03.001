import json

def replay_ai_wins(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        ai_wins = data.get("AI_wins", [])

    for index, game in enumerate(ai_wins):
        print(f"Game {index + 1}:")
        moves = game.split('\r')

        for move in moves:
            if move.strip() != "":
                print(move)
        print("\n")

if __name__ == "__main__":
    replay_ai_wins("simulations.txt")
