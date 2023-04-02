def read_file(file_name):
    results = {}

    with open(file_name, 'r') as file:
        for line in file:
            round_name, *points_str = line.strip().split(';')
            points = [int(point) for point in points_str]
            results[round_name] = points

    return results


def find_average(results):
    total_sum = 0
    total_points = 0

    for round_name, points in results.items():
        average = sum(points) / len(points)
        total_sum += sum(points)
        total_points += len(points)
        print(f"{round_name}: {round(average, 1)}")

    overall_average = round(total_sum / total_points, 1)
    return overall_average


file_name = input()
results = read_file(file_name)
average = find_average(results)
print("The average result over all rounds is: " + str(average))
