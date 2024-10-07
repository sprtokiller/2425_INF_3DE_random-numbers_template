import random
 
def generate_schedule(seed):
    random.seed(seed)

    classes = ["ČJL", "AJN", "OBN", "MAT", "TEV", "INF", "ASW", "POS", "PRG", "MIT", "MSW", "VAP", "   "]
    weekDays = ["Po", "Út", "St", "Čt", "Pá"]

    for day in weekDays:
        schedule = " ".join(random.choice(classes) for _ in range(10))
        print(f"{day}: {schedule}")

generate_schedule(10);


    
    