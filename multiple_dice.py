import random

def roll_multiple_dice(n, k):
    if k <= 0:
        return ValueError
    else:
        for _ in range(n):
            value += random.randint(1, k)

        return value

# Otestování funkce
print(roll_multiple_dice(3, 6))  # Simulace hodu 3 kostkami, každá má 6 hran
