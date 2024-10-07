import random

def roll_multiple_dice(n, k):
    for _ in range(n):
        print(random.randint(0, k))
    return

# Otestování funkce
roll_multiple_dice(3, 6) # Simulace hodu 3 kostkami, každá má 6 hran
