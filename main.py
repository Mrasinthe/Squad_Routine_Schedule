import json


class Squad:
    def __init__(self, rank, s_name, is_driver):
        self.rank = rank
        self.s_name = s_name
        self.is_driver = is_driver


def read_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        patrol_length = lines[0].strip()
        squads = [[]]
        for line in lines[1:]:
            if line.strip() == '':
                squads.append([])
            else:
                rank, s_name, is_driver_str = line.strip().split()
                is_driver = is_driver_str.lower() == "true"
                squads[-1].append(Squad(rank, s_name, is_driver))

    return patrol_length, squads


# def distribute_patrol_hours(total_hours, num_squads):
#     return total_hours // num_squads


def generate_nightly_routine_schedule(patrol_length, squads):
    start_time, end_time = patrol_length.split(' - ')
    start_hour = int(start_time.split(':')[0])
    end_hour = int(end_time.split(':')[0])

    if end_hour < start_hour:
        end_hour += 24

    total_hours = end_hour - start_hour
    # print("total_hours", total_hours)
    # patrol_hours_per_squad = distribute_patrol_hours(total_hours, len(squads))

    routine = {}
    for i, squad in enumerate(squads, start=1):
        squad_name = f"SQUAD #{i}"
        squad_routine = []
        squad_size = len(squad)

        total_patrol_hours = total_hours // squad_size

        num_drivers = sum(1 for soldier in squad if soldier.is_driver)

        if num_drivers < 2:
            print(f"Warning: Squad {squad_name} does not have enough drivers.")
            return None

        for hour in range(start_hour, end_hour):
            hour_str = f"{hour % 24:02}:00"
            squad_routine.append(
                {"Time": hour_str, "Stove-Watch": "", "Patrol": ""})
        for hour, soldier in enumerate(squad, start=start_hour):
            squad_routine[(hour - start_hour)]["Stove-Watch"] = soldier.s_name
            squad_routine[(hour - start_hour)]["Patrol"] = ', '.join(
                [s.s_name for s in squad if s.is_driver]) if soldier.is_driver else '-'
        routine[squad_name] = squad_routine
    return routine


def main():
    input_option = input(
        "Enter 'file' to provide input via file or 'cmd' for command line input: ").strip().lower()
    if input_option == 'file':
        path = input("Enter the file path: ")
        patrol_length, squads = read_file(path)

    elif input_option == 'cmd':
        patrol_length = input(
            "Enter patrol routine length (e.g., 20:00 - 06:00): ")
        print("Enter squad line-ups. Each line should contain: Rank Name Designation (Driver or not). Leave an empty line between squads. Press Enter twice to finish.")
        squads = []
        current_squad = []
        while True:
            line = input()
            if not line.strip() and not current_squad:
                break
            elif not line.strip():
                squads.append(current_squad)
                current_squad = []
            else:
                rank, s_name, is_driver_str = line.strip().split()
                is_driver = is_driver_str.lower() == "true"
                squads[-1].append(Squad(rank, s_name, is_driver))
        if current_squad:
            squads.append(current_squad)

    else:
        print("Invalid input option. Please enter either 'file' or 'cmd'.")
        return

    nightly_routine_schedule = generate_nightly_routine_schedule(
        patrol_length, squads)

    for squad, timetable in nightly_routine_schedule.items():
        print(f"{squad} TIMETABLE")
        print("Time\tStove-Watch\tPatrol")
        for entry in timetable:
            print(
                f"{entry['Time']}\t{entry['Stove-Watch']}\t{entry['Patrol']}")
        print()
    save_file = input(
        "Do you want to save the output as a file? (yes/no): ").lower()
    if save_file == "yes":
        filename = input(
            "Enter the filename to save the output(add '.json' at the end): ")
        with open(filename, "w") as file:
            json.dump(nightly_routine_schedule, file, indent=4)
        print(f"Output saved to {filename}")


if __name__ == "__main__":
    main()
