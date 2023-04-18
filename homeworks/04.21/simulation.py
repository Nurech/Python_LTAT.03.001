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
    wins = defaultdict(int)
    moves_count = []

    num_simulations = 2  # Configure the number of simulations
    print_interval = 1   # Configure the interval for printing running results

    try:
        with open("simulations.txt", "r") as f:
            data = json.load(f)
            wins = defaultdict(int, data["wins"])
            moves_count = data["moves_count"]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

    combined_wins = defaultdict(int)
    for key, value in wins.items():
        combined_wins[int(key)] += value
    wins = combined_wins

    for i in range(len(moves_count) + 1, len(moves_count) + num_simulations + 1):
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
        moves = ' '.join(lines[:-2])  # Exclude the last line (winner) and the empty line before it
        moves += f" Winner: Player {winner}"
        moves_count.append(moves)

        save_to_file(wins, moves_count)  # Save the results after each successful game

        if i % print_interval == 0:
            clear_console()
            print(f"Completed games: {i}")
            print_statistics(wins, moves_count)

def print_statistics(wins, moves_count):
    print("Wins statistics:".center(60, "-"))
    print(f"White (Player 1): {wins[1]}".center(60))
    print(f"Black (Player 2): {wins[2]}".center(60))
    print(f"Draws: {wins[0]}".center(60))
    print()

    print("Win statistics bar chart:".center(60, "-"))
    max_wins = max(wins.values())
    bar_length = 50

    for player, win_count in wins.items():
        if player == 0:
            label = "Draws"
        else:
            label = f"Player {player}"
        bar = "#" * int((win_count / max_wins) * bar_length)
        print(f"{label}: {bar} ({win_count})".ljust(60))
    print("\n" + "-" * 60)


def save_to_file(wins, moves_count):
    data = {
        "wins": dict(wins),
        "moves_count": moves_count
    }

    with open("simulations.txt", "w") as f:
        json.dump(data, f, indent=2, separators=(',', ':'))

if __name__ == "__main__":
    main()
