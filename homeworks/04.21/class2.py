def read_results(filename):
    results = []
    with open(filename, "r") as f:
        for line in f:
            results.append(line.strip().split(";"))
    return results


def who_won(results):
    win_counts = [row.count("W") for row in results]
    max_wins = max(win_counts)
    winning_team = win_counts.index(max_wins) + 1
    return winning_team


def main():
    filename = input("Enter file name: ")
    results = read_results(filename)
    winning_team = who_won(results)
    print(f"Team {winning_team} won the tournament.")


if __name__ == "__main__":
    main()
