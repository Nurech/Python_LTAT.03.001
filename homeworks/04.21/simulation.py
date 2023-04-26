import sys
import subprocess
from collections import defaultdict
import platform
import os
import json

def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    num_simulations = 1000
    print_interval = 10

    data = load_data()
    wins = data["wins"]
    my_wins = data["my_wins"]
    AI_wins = data["AI_wins"]

    for i in range(len(my_wins) + len(AI_wins) + 1, len(my_wins) + len(AI_wins) + num_simulations + 1):
        result = subprocess.run([sys.executable, "game.py"], capture_output=True)
        output = result.stdout.decode('utf-8').strip()

        lines = output.split("\n")
        winner_lines = [line for line in lines if "Player" in line and "won" in line]

        if not winner_lines:
            print(f"Error in game {i}: No winner line found. Skipping this game.")
            continue

        winner_line = winner_lines[0]
        winner = int(winner_line.split()[1])

        wins[winner] += 1
        moves = ' '.join(lines[:-2])

        if winner == 1:
            my_wins.append(moves)
        elif winner == 2:
            AI_wins.append(moves)

        save_to_file(wins, my_wins, AI_wins)

        if i % print_interval == 0:
            clear_console()
            print(f"Completed games: {i}")
            print_statistics(wins)

def print_statistics(wins):
    total_games = sum(wins.values())
    print("Wins statistics:".center(60, "-"))
    print(f"White (Player 1): {wins[1]} ({wins[1] / total_games * 100:.2f}%)".center(60))
    print(f"Black (Player 2): {wins[2]} ({wins[2] / total_games * 100:.2f}%)".center(60))
    print(f"Draws: {wins[0]} ({wins[0] / total_games * 100:.2f}%)".center(60))

    print("Win statistics bar chart:".center(60, "-"))
    max_wins = max(wins.values())
    bar_length = 50

    for player, win_count in wins.items():
        if player == 0:
            label = "Draws"
        else:
            label = f"Player {player}"
        win_percentage = (win_count / total_games) * 100
        bar = "#" * int((win_count / max_wins) * bar_length)
        print(f"{label}: {bar} ({win_count}, {win_percentage:.2f}%)".ljust(60))
    print("" + "-" * 60)


def load_data():
    try:
        with open("simulations.txt", "r") as f:
            data = json.load(f)
            wins_data = data["wins"]
            # Combine wins with the same key
            combined_wins = defaultdict(int)
            for key, value in wins_data.items():
                combined_wins[int(key)] += value
            wins = combined_wins
            my_wins = data["my_wins"]
            AI_wins = data["AI_wins"]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        wins = defaultdict(int, {1: 0, 2: 0, 0: 0})
        my_wins = []
        AI_wins = []

    return {"wins": wins, "my_wins": my_wins, "AI_wins": AI_wins}


def save_to_file(wins, my_wins, AI_wins):
    data = {
        "wins": dict(wins),
        "my_wins": my_wins,
        "AI_wins": AI_wins
    }

    with open("simulations.txt", "w") as f:
        json.dump(data, f, indent=2, separators=(',', ':'))

if __name__ == "__main__":
    main()
