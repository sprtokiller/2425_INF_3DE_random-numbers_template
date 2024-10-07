import random

def generate_schedule(seed):
    random.seed(seed)

    classes = ("CJL", "ANJ", "OBN", "MAT", "TEV", "INF", "ASW", "POS", "PRG", "MIT", "MSW", "VAP", "   ")

    schedule = []

    for day in range(5):
        schedule.append([])
        for _ in range(10):
            schedule[day].append(random.choice(classes))

    return schedule

def print_schedule(schedule):
    print("    1   2   3   4   5   6   7   8   9   10")
    dayID = 0
    for day in schedule:
        print(("Po", "Út", "St", "Čt", "Pá")[dayID], end=": ")
        for lesson in day:
            print(lesson, end=" ")
        print()
        dayID += 1

            

if __name__ == "__main__":
    print_schedule(generate_schedule("UwU"))
