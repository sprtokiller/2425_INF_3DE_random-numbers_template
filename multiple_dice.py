import random

def roll_multiple_dice(n, k):
    # Tvůj kód zde
    i = 0
    while i < n:
        return random.randint(0, k)
        i += 1

# Otestování funkce
print(roll_multiple_dice(3, 6))  # Simulace hodu 3 kostkami, každá má 6 hran
