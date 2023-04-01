file_name = input()
site = input()

bird_data = []
total_birds = 0

with open(file_name, "r") as f:
    while True:
        species = f.readline().strip()
        if not species:
            break
        location = f.readline().strip()
        count = f.readline().strip()
        count = int(count)
        bird_data.append((species, location, count))
        total_birds += count

site_birds = [b for b in bird_data if b[1] == site]

if site_birds:
    print(f"Birds at the observation site '{site}':")
site_total = 0
site_species = 0
for bird in site_birds:
    print(f"{bird[0]}: {bird[2]}")
    site_total += bird[2]
    site_species += 1
    print(f"There were {site_total} birds and {site_species} bird species at this site.")
    percentage = (site_total / total_birds) * 100
    print(f"{percentage:.2f}% of all birds were observed at this site.")

with open("observed.txt", "w") as f:
    f.write(f"A total of {total_birds} birds were observed.\n")
    f.write(f"{len(bird_data)} bird species were found.\n")
    if site_species > 0:
        f.write(f"{site_species} bird species were observed at the observation site '{site}'.\n")
    else:
        print(f"Birds at the observation site '{site}':")
        print("There is no such observation site.")
        with open("observed.txt", "w") as f:
            f.write(f"A total of {total_birds} birds were observed.\n")
            f.write(f"{len(bird_data)} bird species were found.\n")
