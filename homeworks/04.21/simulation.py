import itertools
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

def load_settings():
    with open("settings.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        settings = {}
        for line in lines:
            key, value = line.split(" = ")
            settings[key] = int(value)
        return settings

def update_settings_file(settings):
    with open("settings.txt", "w") as f:
        for key, value in settings.items():
            f.write(f"{key} = {value}\n")

import random

def update_settings(settings):
    for key, value in settings.items():
        new_value = random.randint(1, 10)
        settings[key] = new_value
    update_settings_file(settings)



def load_sim_stats():
    if not os.path.exists("sim_stats.txt"):
        return {}

    with open("sim_stats.txt", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    return data

def save_sim_stats(data):
    with open("sim_stats.txt", "w") as f:
        json.dump(data, f, indent=2)

def main():
    num_simulations = 10000
    print_interval = 200
    num_games_per_config = 200
    update_interval = num_games_per_config

    settings = load_settings()
    sim_stats = load_sim_stats()

    for i in range(1, num_simulations + 1):
        if i % update_interval == 1:
            update_settings(settings)
            print(settings)


        config_key = json.dumps(settings, sort_keys=True)

        if config_key not in sim_stats:
            sim_stats[config_key] = {
                "wins": defaultdict(int, {1: 0, 2: 0, 0: 0}),
                "my_wins": [],
                "AI_wins": [],
            }

        config_data = sim_stats[config_key]

        result = subprocess.run([sys.executable, "game.py"], capture_output=True)
        output = result.stdout.decode('utf-8').strip()

        lines = output.split("\n")
        winner_lines = [line for line in lines if "Player" in line and "won" in line]

        if not winner_lines:
            print(f"Error in game {i}: No winner line found. Skipping this game.")
            continue

        winner_line = winner_lines[0]
        winner = int(winner_line.split()[1])

        config_data["wins"][winner] += 1
        moves = ' '.join(lines[:-2])

        if winner == 1:
            config_data["my_wins"].append(moves)
        elif winner == 2:
            config_data["AI_wins"].append(moves)

        save_sim_stats(sim_stats)

        if i % print_interval == 0:
            clear_console()
            print(f"Completed games: {i}")
            print_statistics(config_data["wins"])

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
