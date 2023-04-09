def birds(filename):
    my_list = {}
    with open(filename, 'r') as file:
        for line in file:
            bird, freq = line.strip().split(',')
            my_list[bird] = int(freq)
    return my_list


def main():
    file_name = input("Enter filename: ") or "birds.txt"
    bird_dict = birds(file_name)

    freq = int(input("Enter target frequency: ")) or "2"

    total_birds = 0
    for bird, freq in bird_dict.items():
        total_birds += freq
        if freq > freq:
            print(f"{bird} ({freq})")

    print(f"Juku saw {total_birds} birds outside.")


main()
