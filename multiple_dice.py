import random

def roll_multiple_dice(n, k):
    for _ in range(1, n):
        random.randint(1, k)
    return

# Otestování funkce
print(roll_multiple_dice(3, 6))  # Simulace hodu 3 kostkami, každá má 6 hran
