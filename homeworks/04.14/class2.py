import os


def read_participants(event_number):
    all = set()
    event_data = {}

    for i in range(1, event_number + 1):
        file_name = f"event{i}.txt"
        if not os.path.exists(file_name):
            print(f"File {file_name} not found. Skipping.")
            continue

        with open(file_name, "r") as file:
            curr = {line.strip() for line in file}

        newcomrs = curr - all
        recurring = curr & all if i > 1 else set()

        event_data[i] = {
            "participants": curr,
            "newcomrs": newcomrs,
            "recurring": recurring
        }

        # bitwise OR https://stackoverflow.com/a/14295472/15439733
        all |= curr

    return event_data


def main():
    event_count = int(input("Enter numer of events: "))
    event_data = read_participants(event_count)

    print('\n')

    all_participants = set.union(*[event["participants"] for event in event_data.values()])
    print("Participants who took part in at least one event:")
    for participant in sorted(all_participants):
        print(participant)

    reoccur = set.union(*[event["recurring"] for event in event_data.values()])
    print('\n')
    print("The people who participated in two consecutive events are:")
    for participant in sorted(reoccur):
        print(participant)

    most_new_evnt = max(event_data, key=lambda x: len(event_data[x]["newcomrs"]) if x > 1 else 0)
    most_newcomers = len(event_data[most_new_evnt]["newcomrs"])
    print('\n')
    print(f"Event {most_new_evnt} atrracted the most number of newcomrs, {most_newcomers} newcomrs.")


main()
