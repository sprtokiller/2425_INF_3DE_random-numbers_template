import random

def roll_die(k):
    if k <= 0:
        return ValueError
    else:
        return random.randint(1, k)

# Otestování funkce
print(roll_die(6))  # Simulace hodu 6-hranou kostkou
