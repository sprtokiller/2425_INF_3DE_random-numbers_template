import random

def roll_multiple_dice(n, k):
    # Tvůj kód zde
    for _ in range(n):
        print(random.randrange(1, k));

# Otestování funkce
print(roll_multiple_dice(3, 6))  # Simulace hodu 3 kostkami, každá má 6 hran
