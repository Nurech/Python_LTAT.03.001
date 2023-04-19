import sys
import subprocess
import platform
import os
import json
import random

global keys
keys = [
    "grouping_weight",
    "capture_weight",
    "center_weight",
    "fork_weight",
    "defense_weight",
    "objective_weight",
    "block_fork_weight",
    "safe_move_weight",
    "edge_weight",
    "corner_weight",
    "avoid_opportunity_weight",
]
def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")


def load_previous_configs():
    try:
        with open("best_config.txt", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def save_configs(configs):
    with open("best_config.txt", "w") as f:
        json.dump(configs, f, indent=2)


def generate_config_based_on_previous_configs(previous_configs):
    if not previous_configs:
        return generate_random_config()

    def get_trend(configs, key):
        if len(configs) < 2:
            return 0
        trend = 0
        for i in range(1, len(configs)):
            trend += configs[i][key] - configs[i - 1][key]
        return trend / (len(configs) - 1)

    sorted_configs = sorted(previous_configs, key=lambda x: x["config_score"], reverse=True)
    config = {}
    no_change = True
    for key in keys:
        trend = get_trend(sorted_configs, key)
        adjustment = 1 if trend > 0 else -1 if trend < 0 else 0
        config[key] = max(1, min(10, sorted_configs[0][key] + adjustment))
        if adjustment != 0:
            no_change = False

    if no_change:
        key_to_change = random.choice(keys)
        config[key_to_change] = max(1, min(10, config[key_to_change] + random.choice([-1, 1])))

    return config


def generate_random_config():
    return {
        "grouping_weight": random.randint(1, 10),
        "capture_weight": random.randint(1, 10),
        "center_weight": random.randint(1, 10),
        "fork_weight": random.randint(1, 10),
        "defense_weight": random.randint(1, 10),
        "objective_weight": random.randint(1, 10),
        "block_fork_weight": random.randint(1, 10),
        "safe_move_weight": random.randint(1, 10),
        "edge_weight": random.randint(1, 10),
        "corner_weight": random.randint(1, 10),
        "avoid_opportunity_weight": random.randint(1, 10),
    }


def main():
    total_simulations = 100000
    simulations_per_config = 10
    num_configs = total_simulations // simulations_per_config

    previous_configs = load_previous_configs()

    for config_index in range(num_configs):
        config = generate_config_based_on_previous_configs(previous_configs)
        wins = 0
        losses = 0

        for sim_index in range(simulations_per_config):
            result = subprocess.run([sys.executable, "game.py", json.dumps(config)], capture_output=True)
            output = result.stdout.decode('utf-8').strip()

            lines = output.split("\n")
            winner_lines = [line for line in lines if "Player" in line and "won" in line]

            if not winner_lines:
                print(f"Error in game {sim_index}: No winner line found. Skipping this game.")
                continue

            winner_line = winner_lines[0]
            winner = int(winner_line.split()[1])

            if winner == 1:  # Assuming you are Player 1
                wins += 1
            else:
                losses += 1

        win_percentage = (wins / simulations_per_config) * 100
        config["num_simulations"] = simulations_per_config
        config["win_percentage"] = win_percentage
        config["config_score"] = win_percentage * simulations_per_config
        previous_configs.append(config)

        previous_configs.sort(key=lambda x: x["config_score"], reverse=True)
        save_configs(previous_configs)

        best_config = previous_configs[0]
        print(f"After {config_index + 1} configurations:")
        print("Best configuration:")
        print(json.dumps(best_config, indent=2))
        print(
            f"Best Winning percentage: {best_config['win_percentage']:.2f}% (Total Wins: {int(best_config['win_percentage'] * best_config['num_simulations'] / 100)}, Total Losses: {best_config['num_simulations'] - int(best_config['win_percentage'] * best_config['num_simulations'] / 100)})")
        print(f"Current configuration win percentage: {win_percentage:.2f}% (Wins: {wins}, Losses: {losses})")


if __name__ == "__main__":
    main()
