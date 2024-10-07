import random

def generate_schedule(seed):
    random.seed(seed)  # to run the randomization the same

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    lesson_limits = { 
        "Český jazyk a literatura": 3,
        "Anglický jazyk": 3,
        "Občanská nauka": 1,
        "Matematika": 4,
        "Tělesná výchova": 2,
        "Informatika": 2,
        "Aplikační Software": 2,
        "Počítačové sítě": 3,
        "Programování": 3,
        "Mikroprocesorová technika": 2,
        "Multimediální software": 2,
        "Vývoj aplikací": 2,
        "Volná hodina": 5
    }
    
    lessons = []  # empty array 
    for lesson, limit in lesson_limits.items():  # loop with a limit based on the assigned limits
        lessons.extend([lesson] * limit)  # adds the lessons their designated amount of times
    
    random.shuffle(lessons)  # random schedule maker

    for day in days:  # print which day it is
        print(f"\nSchedule for {day}:")
        lessons_today = set()
        
        for _ in range(7):  # print the lessons
            if lessons:  
                lesson = lessons.pop() #remove it so it counts it in
                if lesson not in lessons_today: #check if the lesson is not in the day already
                    lessons_today.add(lesson) 
                    print(lesson)

generate_schedule(10)
